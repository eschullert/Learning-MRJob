# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for w in words:
            yield w.lower(),1

    def reducer(self, key, values):
        lst = list(values)
        yield key, len(lst)

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
