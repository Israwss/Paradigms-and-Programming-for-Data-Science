import numpy as np
from sympy import Matrix,symbols, simplify #Computo simbolico
import matplotlib.pyplot as plt
def clasif_e(samples):
  '''
  Clasificador determinista euclideano
  '''
  n_samples = len(samples)
  # Vector generico usando sympy
  X=Matrix(['x'+str(i+1) for i in range(samples[0].shape[0])])
  # Matriz de distancias
  fds=[]
  for s in samples:
    m=Matrix(np.mean(s,axis=1))
    fds.append(simplify(X.T*m-(m.T*m)/2))
  return fds

# w1=(0.5, 10.5) , (1, 12.5) , (3, 10.5) , (3, 12.5) , (3, 14.5) , (3, 18) , (5, 18) , (5, 16) , (5, 14.5) , (5, 13)
w1=np.array([[0.5,10.5],[1,12.5],[3,10.5],[3,12.5],[3,14.5],[3,18],[5,18],[5,16],[5,14.5],[5,13]]).T
# w2 =(6, 9) , (8, 10) , (9, 11) , (8.5, 12) , (7, 13.5) (8, 16)
w2=np.array([[6,9],[8,10],[9,11],[8.5,12],[7,13.5],[8,16]]).T
samples=(w1,w2)
fds=clasif_e(samples)
print(fds)

for fd in range(len(fds)):
  print(f'{fd} {fd+1}: {fds[fd].evalf(subs={"x1":3,"x2":1,"x3":3,"x4":1})}')




