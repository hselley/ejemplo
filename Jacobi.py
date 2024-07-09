import numpy as np
from numpy import linalg as la
from prettytable import PrettyTable

def Jacobi(A, b, TOL=1e-2, Nmax=50): # 1e-2 = 1x10^(-2)
    n = len(A)
    x0 = np.zeros(n)    # Vector inicial
    x = np.zeros(n)     # Vector para aproximaciones
    
    names = []
    names.append('i')
    for i in range(n):
        names.append('x' + str(i+1))
    
    # Creación de la tabla vacía con el encabezado dado por 'names'
    res = PrettyTable(field_names=names)

    # Rutina principal
    k = 1
    while k<=Nmax:
        for i in range(n):
            suma = 0
            for j in range(n):
                if j!=i:
                    suma = suma + A[i,j]*x0[j]
            x[i] = (-suma + b[i])/A[i,i]
        res.add_row([k] + x.tolist())

        if la.norm(x-x0)<TOL:
            return(print(res))
    
        k += 1
        x0 = np.copy(x)
    print(f'El método fracasó luego de {Nmax} iteraciones')

A = np.array([[3,-1,1], [3,6,2], [3,3,7]])
b = np.array([1,0,4])

Jacobi(A, b)