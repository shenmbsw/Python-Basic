# AUTHOR Shen Shen shs2016f@bu.edu
# AUTHOR You Han yhan94@bu.edu

from numpy import zeros,exp,array,pi

def DFT(x):
    if isinstance(x,list):
        ipar=getdatalist(x)
    elif isinstance(x,tuple):
        ipar=getdatatuple(x)
    elif type(x)==type(zeros(1)):
        ipar= x
    else:
        raise ValueError(' input value is not a sequence of numerical values')
    print("ipar:",ipar)
    L = len(ipar)
    y = zeros(L, complex)
    for n in range(0, L):
        for m in range(0, L):
            a = ipar[m] * exp(-2j * pi * m * n / L)
            y[n] += a
    return y

def getdatalist(ls):
    L=len(ls)
    a=zeros(L,complex)
    for i in range(L):
        b=complex(ls[i])
        a[i]=b
    return a
    
def getdatatuple(tup):
    L=len(tup)
    a=zeros(L,complex)
    for i in range(L):
        b=complex(tup[i])
        a[i]=b
    return a

def main():
    x = array([2+2j,2,2,1])
    y = DFT(x)
    print(y)

    
if __name__=="__main__":
    main()
