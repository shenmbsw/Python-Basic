
# AUTHOR ShenShen shs2016f@bu.edu
import math

Z=0

try:
    X = int(input("Enter the first integer: "))
except ValueError:
    print("Error, please enter a positive integer")
    exit()
if int(X)<0:
    print ('Error, please enter a positive integer')
    exit()

try:
    Y = int(input("Enter the second integer: "))
except ValueError:
    print("Error, please enter a positive integer")
    exit()
if int(Y)<0:
    print ('Error, please enter a positive integer')
    exit()


a=1
b=1
if X>0:
    while X>1:
        a=a*X
        X=X-1
if Y>0:
    while Y>1:
        b=b*Y
        Y=Y-1
Z=int(a-b)
if Z>=0:
    print (Z,len(str(Z)),math.ceil(Z.bit_length()/8))
else:
    print (Z,len(str(Z))-1,math.ceil(Z.bit_length()/8))
