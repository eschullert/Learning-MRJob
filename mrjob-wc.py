# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        c = len(line)
        w = len(line.split())
        l=1
        yield ('chars', c+1)
        yield ('words', w)
        yield ('lines', l)

    def reducer(self, key, values):  # values is a generator
        ans = sum(list(values))
        yield key, ans

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
