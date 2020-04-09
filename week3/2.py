import random

class Matrix():
    def __init__(self, n):
        self.n = n
        self.rows = [[random.randint(0,9) for i in range(n)] for j in range(n)]
        
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'
    
    def transpose(self):
        mtrx = Matrix(self.n)
        mtrx.rows =  [list(item) for item in zip(*self.rows)]
        return mtrx
    
    def getdim(self):
        return self.n

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item
    
    def __add__(self, mtrx):
        if self.getdim() != mtrx.getdim():
            print('Operation impossible')
            return None
        else:
            resmtrx = Matrix(self.n)
            for i in range(self.n):
                row = [sum(item) for item in zip(self.rows[i], mtrx[i])]
                resmtrx[i] = row
            return resmtrx
        
    def __mul__(self, mtrx):
        if self.getdim() != mtrx.getdim():
            print('Operation impossible')
            return None
        else:
            matr_t = mtrx.transpose()
            resmtrx = Matrix(self.n)
            for x in range(self.n):
                for y in range(self.n):
                    resmtrx[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], matr_t[y])])
            return resmtrx


m1 = Matrix(3)
print("Matrix m1:")
print(m1)
m2 = m1.transpose()
print("Matrix m2 (transpose m1)")
print(m2)
m3 = m1 + m2
print("Matrix m3 (addition of m1 and m2)")
print(m3)
m4 = m1 * m3
print("Matrix m4 (multiplication of m1 and m3)")
print(m4)