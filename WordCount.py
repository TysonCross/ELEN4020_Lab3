from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class WordCount(MRJob):
    FILES = ['stop_words.txt']
    SORT_VALUES = True

    def configure_args(self):
        super(WordCount, self).configure_args()
        self.add_file_arg(
            '--stop-words',
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
                combiner=self.combiner,
                reducer=self.reducer,
            ),
            MRStep(
                reducer=self.reducer_sort_counts,
            )
        ]

    def mapper_init(self):
        with open(self.options.stop_words) as f:
            self.stop_words = set(line.strip() for line in f)

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            word = word.lower()
            if word not in self.stop_words:
                yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, key, values):
        yield None, (sum(values), key)

    def reducer_sort_counts(self, _, word_counts):
        for count, key in sorted(word_counts, reverse=True):
            yield (count, key)

if __name__ == '__main__':
    WordCount.run()
