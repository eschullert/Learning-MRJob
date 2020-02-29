# Plantilla para escribir trabajos de MapReduce usando MRJob
# Para correrlo usar en terminal:  python mrjob-template.py <input file>  -q

from mrjob.job import MRJob
from mrjob.step import MRStep

# Nombre de la clase
class MR_program(MRJob):

    def mapper(self, _, line):
        # yield key, value
        pass

    def reducer(self, key, values):  # Los valores son un generador
        # yield key, f(values)
        pass

if __name__ == '__main__':
    # Cambiar a nombre de la clase que se utilizó arriba
    MR_program.run()
    
