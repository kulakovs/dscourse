import random
import math

class Matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.rows = [[random.randint(0,9) for i in range(m)] for j in range(n)]
        
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'
    
    def transpose(self):
        m, n = self.n, self.m
        mtrx = Matrix(n, m)
        mtrx.rows =  [list(item) for item in zip(*self.rows)]
        return mtrx
    
    def getdim(self):
        return (self.n, self.m)

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item
    
    def __add__(self, mtrx):
        if self.getdim() != mtrx.getdim():
            print('Operation impossible')
            return None
        else:
            resmtrx = Matrix(self.n, self.m)
            for i in range(self.n):
                row = [sum(item) for item in zip(self.rows[i], mtrx[i])]
                resmtrx[i] = row
            return resmtrx
        
    def __mul__(self, mtrx):
        muln, mulm = mtrx.getdim()
        if self.n != mulm:
            print('Operation impossible')
            return None
        else:
            matr_t = mtrx.transpose()
            resmtrx = Matrix(self.n, mulm)
            for x in range(self.n):
                for y in range(mulm):
                    resmtrx[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], matr_t[y])])
            return resmtrx

class Vector(Matrix):
    def __init__(self, n):
        Matrix.__init__(self, 1, n)
        
    def __mul__(self, vctr):
        if self.getdim() != vctr.getdim():
            print('Operation impossible')
            return None
        else:
            for x in range(self.n):
                res = sum([item[0]*item[1] for item in zip(self.rows[x], vctr[x])])
            return res
    def norm(self):
        for x in range(self.n):
            res = sum([item[0]*item[1] for item in zip(self.rows[x], self.rows[x])])
        return math.sqrt(res)

v1 = Vector(5)
print("Vector v1:")
print(v1)

v2 = Vector(5)
print("Vector v2:")
print(v2)

v3 = v1 + v2
print("Vector v3 (addition of vectors v1 and v2):")
print(v3)

v4 = Vector(3)
print("Addition of different dimension vectors. Error.")
v5 = v1 + v4


print("Multiplication of vectors v1 and v2: ")
v6 = v1 * v2
print(v6)

print("Euclidean norm of vector v1: ")
print(v1.norm())
