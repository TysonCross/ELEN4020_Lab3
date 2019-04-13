from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")
MRJob.SORT_VALUES = True


class WordLineFreq(MRJob):
    FILES = ['text/stop_words.txt']

    def steps(self):
        JOBCONF_STEP1 = {
            'stream.num.map.output.key.fields':2
        }
        return [
            MRStep(jobconf=JOBCONF_STEP1,
                mapper_init=self.mapper_init,
                mapper=self.mapper_get_words,
                reducer=self.reducer,
            )
        ]

    def mapper_init(self):
        with open('stop_words.txt') as f:
            self.stop_words = set(line.strip() for line in f)

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            word = word.lower()
            if word not in self.stop_words:
                yield (word.lower(), line)

    def reducer(self, key, values):
        a = [v for v in values]
        yield (a, key)

if __name__ == '__main__':
    WordLineFreq.run()
    