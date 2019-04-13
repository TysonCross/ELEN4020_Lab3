from mrjob.job import MRJob
from mrjob.step import MRStep
import sys
import re

WORD_RE = re.compile(r"[\w']+")


class WordLineFreq(MRJob):
    FILES = ['stop_words.txt']
    SORT_VALUES = True

    def configure_args(self):
        super(WordLineFreq, self).configure_args()
        self.add_file_arg(
            '--stop-words',
            metavar='STOP_WORDS_FILE',
            dest='stop_words',
            type=str,
            default='stop_words.txt',
            help='Input stop words text file')
        self.add_passthru_arg(
            '--limit',
            metavar='K',
            dest='K',
            type=int,
            default=10,
            help='Number of words to return')

    def steps(self):
        JOBCONF_STEP1 = {
            'stream.num.map.output.key.fields':1
        }
        return [
            MRStep(jobconf=JOBCONF_STEP1,
                mapper_init=self.mapper_init,
                mapper=self.mapper_get_words,
                reducer=self.reducer,
            )
        ]

    def mapper_init(self):
        with open(self.options.stop_words) as f:
            self.stop_words = set(line.strip() for line in f)

    def mapper_get_words(self, _, line):
        sys.stderr.write("MAPPER INPUT: ({0})\n".format(line))  # debug
        for word in WORD_RE.findall(line):
            word = word.lower()
            if word not in self.stop_words:
                line_num = line
                # line_num = [v for v in line]
                # line_num = line.index(line)
                yield (word.lower(), line_num)

    def reducer(self, key, values):
        sys.stderr.write("REDUCER INPUT: ({0},{1})\n".format(key,values)) # debug
        line = [v for v in values] # generator -> list
        yield (key, line)

if __name__ == '__main__':
    WordLineFreq.run()
    