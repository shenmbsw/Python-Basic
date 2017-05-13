# AUTHOR ShenShen shs2016f@bu.edu
# w2c_addinghalf.py

from math import inf

def number_from_half(s : str):
	a=int(s,16)
	b="{0:b}".format(a) 	#b is a string
	bin_half=list('0000000000000000')
	i=1
	while i<=len(b):
		bin_half[-i]=b[-i]	#turn string b into list bin_half
		i=i+1
	Lsign=bin_half[0]
	Lexp=bin_half[1:6]
	Lfra=bin_half[6:16]
	sign = ''.join(Lsign)		#sign,exp and fra are str
	exp = ''.join(Lexp)
	fra = ''.join(Lfra)
	x=0				#a=1.len(a is a float)
	a=1
	while x<len(fra):
		if fra[x]=='1':
			a=a+0.5**(x+1)
		x=x+1
	
	intexp=int(exp,2)		#b=exp-15
	b=intexp-15
	s=int(sign)

	if b==-15:			#str "Lsign" design the sign
		return ((-1)**s)*(2**-14)*(a-1)
	else:
		return ((-1)**s)*(2**b)*a
	
def main():
	h=0
	while(1):
		s=input()
		try:
			h=h+number_from_half(s)
		except:
			s=='exit'
			break	
	print(h)
if __name__ == '__main__':
    main()
