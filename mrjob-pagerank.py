# Template for writing MapReduce programs using mrjob
# % python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):
    def mapper(self, _, line):
        node, pr, *nbrs = line.split()
        pr=float(pr)
        for x in nbrs:
            yield x, pr/len(nbrs)
        yield node, nbrs


    def reducer_1(self, key, values):  # values is a generator
        lst = list(values)
        acc = 0
        for x in lst:
            if type(x) == list:
                nbrs = x
            else:
                acc += x
        pr = (1-0.85)/4 + 0.85*acc
        for z in nbrs:
            yield z, pr/len(nbrs)
        yield key,nbrs

    def reducer_2(self, key, values):  # values is a generator
        lst = list(values)
        acc = 0
        for x in lst:
            if type(x) == list:
                nbrs = x
            else:
                acc += x
        pr = (1-0.85)/4 + 0.85*acc
        yield key, pr
        
    def steps (self):
        return ([MRStep(mapper=self.mapper)]
                +[MRStep(reducer=self.reducer_1)]*30
                +[MRStep(reducer=self.reducer_2)]
               )

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
