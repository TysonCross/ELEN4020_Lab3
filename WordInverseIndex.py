from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep
import sys
import re

WORD_RE = re.compile(r"[\w']+")

class WordInverseIndex(MRJob):
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
                                default=50,
                                help='Number of words to return')

    def steps(self):
        return [
            MRStep(
                mapper_init=self.mapper_init,
                mapper_raw=self.mapper_raw,
                reducer=self.reducer,
            )
        ]

    def mapper_init(self):
        # sys.stderr.write("MAPPER_INIT INPUT: ({0})\n".format(INPUT))
        with open(self.options.stop_words) as f:
            self.stop_words = set(line.strip() for line in f)

    def mapper_raw(self, path, _):
            with open(path, 'r') as f:
                for num, line in enumerate(f):
                    if num>= self.options.K: break
                    for word in line.rstrip().split():
                        word = word.lower()
                        if word not in self.stop_words:
                            yield (word.lower(), num) # optionally, can pass [num, line.rstrip()]

    def reducer(self, key, values):
        line = [v for v in values]
        # sys.stderr.write("output: ({0})\n".format(line))
        yield (key, ','.join( str(a) for a in line ))

if __name__ == '__main__':
    WordInverseIndex.run()
