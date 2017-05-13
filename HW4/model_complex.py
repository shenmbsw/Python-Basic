# -*- coding: utf-8 -*-

class Complex():
    "Complex(real,[imag]) -> a complex number"

    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag

    def __abs__(self):
        "abs(self)"
        return (self.real**2 +self.imag**2)**0.5
        
    def __mul__(s,v):
        
        if hasattr(v,'imag'):
            x = s.real * v.real - s.imag * v.imag
            y = s.real * v.imag + v.real * s.imag
            return Complex(x,y)
        else:
            return Complex(v*s.real,v*s.imag)

    def __add__(self,value):
      
        if hasattr(value,'imag'):
            return Complex(self.real+value.real,self.imag+value.imag)
        else:
            return Complex(self.real+value,self.imag)            



    def __rmul__(s,v):
      
        if hasattr(v,'imag'):
            x = s.real * v.real - s.imag * v.imag
            y = s.real * v.imag + v.real * s.imag
            return Complex(x,y)
        else:
            return Complex(v*s.real,v*s.imag)

    def __radd__(self,value):
        
        if hasattr(value,'imag'):
            return Complex(self.real+value.real,self.imag+value.imag)
        else:
            return Complex(self.real+value,self.imag)            

    def __str__(self):
        if self.real==0:
            return "{}j".format(self.imag)
        else:
            sign="-" if self.imag<0 else "+"
            return "({}{}{}j)".format(self.real,sign,abs(self.imag))

    def __repr__(self):
        return str(self)

    def __pow__(self,value):
        "Return self ** value"
        raise NotImplementedError('not done yet')
        