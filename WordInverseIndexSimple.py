from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime
import sys
import re

WORD_RE = re.compile(r"[\w']+")
MRJob.SORT_VALUES = True


class WordInverseIndexSimple(MRJob):
    FILES = ['stop_words.txt']
    SORT_VALUES = True

    def configure_args(self):
        super(WordInverseIndexSimple, self).configure_args()
        self.add_file_arg(  '--stop-words',
                            metavar='STOP_WORDS_FILE',
                            dest='stop_words',
                            type=str,
                            default='stop_words.txt',
                            help='Input stop words text file')

    def steps(self):
        return [
            MRStep(
                mapper_init=self.mapper_init,
                mapper=self.mapper_get_words,
                reducer=self.reducer,
            )
        ]

    def mapper_init(self):
        with open(self.options.stop_words) as f:
            self.stop_words = set(line.strip() for line in f)

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            word = word.lower()
            if word not in self.stop_words:
                yield (word.lower(), line)

    def reducer(self, key, values):
        for index, lines in enumerate(values):
            if index == 50: break
            yield (key, lines)

    def reducer_sort_counts(self, _, values):
        for key, lines in sorted(values):
            yield (key, lines)

if __name__ == '__main__':
    start_time = datetime.now()
    WordInverseIndexSimple.run()
    end_time = datetime.now()
    elapsed_time = (end_time - start_time)*1000
    sys.stderr.write("Total Seconds WordInverseIndexSimple.py: ({0}) microseconds\n".format(elapsed_time.total_seconds()))