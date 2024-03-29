from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime
import sys
import re

WORD_RE = re.compile(r"[\w']+")

class WordFreq(MRJob):
    ''' This function returns the top K frequency occurrences of words in a provided text.
        The number of words may be greater or less than K, depending if there are several words with
        the same number of occurrences in the text, or if there are fewer words than K in the text. '''

    FILES = ['stop_words.txt']
    SORT_VALUES = True

    def configure_args(self):
        super(WordFreq, self).configure_args()
        self.add_passthru_arg(
            '--limit',
            metavar='K',
            dest='K',
            type=int,
            default=10,
            help='Input stop words text file')
        self.add_file_arg(
            '--stop-words',
            metavar='STOP_WORDS_FILE',
            dest='stop_words',
            type=str,
            default='stop_words.txt',
            help='Number of highest occurances to return')

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
        K = self.options.K
        i = 0
        last_freq = 0
        current_freq = 0
        for count, key in sorted(word_counts, reverse=True):
            if (i==K):
                current_freq = int(count)
            if(i < K):
                last_freq = current_freq
                current_freq = int(count)
                if (last_freq != current_freq):
                    i+=1
                yield (count, key)

if __name__ == '__main__':
    start_time = datetime.now()
    WordFreq.run()
    end_time = datetime.now()
    elapsed_time = (end_time - start_time)*1000
    sys.stderr.write("Total Seconds WordFreq.py: ({0}) microseconds\n".format(elapsed_time.total_seconds()))