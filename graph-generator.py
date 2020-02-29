import string
import random

n_nodes=random.randint(0,21)
print(26-n_nodes)
lst=string.ascii_uppercase[:-n_nodes]
with open('graph-2.txt','w') as f:
    for i in lst:
        f.write(i+' ')
        f.write(str(1/len(lst)))
        letters_left=list(lst)
        letters_left.remove(i)
        for j in range(random.randint(0,len(letters_left))):
            l=random.choice(letters_left)
            letters_left.remove(l)
            f.write(' '+l)
        f.write('\n')