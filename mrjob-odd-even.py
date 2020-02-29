from mrjob.job import MRJob
from mrjob.step import MRStep

# change the name of the class
class MR_program(MRJob):

    def mapper(self, _, line):
        i = int(line)
        if i%2==0:
            tag = 'even'
        else:
            tag = 'odd'
        yield tag,i

    def reducer(self, key, values):  # values is a generator
        lst = list(values)
        ans = sum(lst)
        yield key, ans

if __name__ == '__main__':
    # change to match the name of the class
    MR_program.run()
    
