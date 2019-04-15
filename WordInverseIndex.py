from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime
import itertools
import sys
import re

WORD_RE = re.compile(r"[\w']+")

class WordInverseIndex(MRJob):
    ''' Returns the inverse index of the words in the first K lines in the input text'''

    FILES = ['stop_words.txt']
    SORT_VALUES = True
    
    def configure_args(self):
        super(WordInverseIndex, self).configure_args()
        self.add_file_arg(  '--stop-words',
                                metavar='STOP_WORDS_FILE',
                                dest='stop_words',
                                type=str,
                                default='stop_words.txt',
                                help='Input stop words text file')
        self.add_passthru_arg(  '--limit',
                                metavar='K',
                                dest='K',
                                type=int,
                                default=-1,
                                help='Number of lines of the text to process')
        self.add_passthru_arg(  '--index-limit',
                                metavar='L',
                                dest='L',
                                type=int,
                                default=-1,
                                help='Number of indexed lines per word to return')

    def steps(self):
        return [
            MRStep(
                mapper_init=self.mapper_init,
                mapper_raw=self.mapper_raw,
                reducer=self.reducer,
            ),
            MRStep(
                reducer=self.reducer_sort_counts,
            )
        ]

    def mapper_init(self):
        with open(self.options.stop_words) as f:
            self.stop_words = set(line.strip() for line in f)

    def mapper_raw(self, path, _):
            with open(path, 'r') as f:
                for num, line in enumerate(f,1):
                    if (self.options.K!=-1) & (num >= self.options.K): break
                    for word in WORD_RE.findall(line):
                        word = word.lower()
                        if word not in self.stop_words:
                            yield (word.lower(), num) # optionally, can pass [num, line.rstrip()]

    def reducer(self, key, values):
        if (self.options.L==-1):
            lines_list = list(values)
        else: 
            lines_list = list(itertools.islice(values, self.options.L)) #
        yield None,(key, ','.join( str(line) for line in lines_list ))
    
    def reducer_sort_counts(self, _, values):
        for key, lines in sorted(values):
            yield (key, lines)

if __name__ == '__main__':
    start_time = datetime.now()
    WordInverseIndex.run()
    end_time = datetime.now()
    elapsed_time = (end_time - start_time)*1000
    sys.stderr.write("Total Seconds WordInverseIndex.py: ({0}) microseconds\n".format(elapsed_time.total_seconds()))
