# AUTHOR ShenShen shs2016f@bu.edu
# -*- coding: utf-8 -*-

class Polynomial():

    def __init__(self,coef=[complex(0,0)]):
        Maxexp = len(coef)
        self.elements = {}
        for i in range(0,Maxexp):
            if complex(coef[i]) != complex(0,0):
                self.elements[Maxexp-i-1] = coef[i]

    def __setitem__(self, nexp, ncoef):
        self.elements[nexp] = ncoef

    def __getitem__(self, exp):
        if exp in self.elements:
            return self.elements[exp]
        return complex(0,0)

    def __add__(a,b):
        c=Polynomial()
        c.elements=dict.copy(a.elements)
        for i in dict.keys(b.elements):
            if i in c.elements:
                c.elements[i] += b.elements[i]
            else:
                c.elements[i] = b.elements[i]
        return c

    def __sub__(a,b):
        c=Polynomial()
        c.elements=dict.copy(a.elements)
        for i in dict.keys(b.elements):
            if i in c.elements:
                c.elements[i] -= b.elements[i]
            else:
                c.elements[i] = (0-b.elements[i])
        return c

    def __mul__(a,b):
        c = Polynomial()
        c.elements = {}
        for i in dict.keys(a.elements):
            for j in dict.keys(b.elements):
                if (i + j) in c.elements:
                    c.elements[(i+j)] += (a.elements[i] * b.elements[j])
                else:
                    c.elements[(i+j)] = (a.elements[i] * b.elements[j])
        return c

    def __eq__(self, other):
        try:
            for i in dict.keys(self.elements):
                if self.elements[i] != other.elements[i]: 
                    return False
        except KeyError:
            if (self.elements[i]!=0):
                return False
        return True

    def eval(self, value):
        result = 0
        for i in dict.keys(self.elements):
            result += self.elements[i]*value**i
        return result

    def deriv(self):
        result = Polynomial()
        for i in dict.keys(self.elements):
            if i != 0: 
                result.elements[i-1] = (i * self.elements[i])
        return result

def main():
    pass

if __name__=="__main__":
	main()