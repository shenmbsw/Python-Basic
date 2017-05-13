# AUTHOR ShenShen shs2016f@bu.edu
# AUTHOR Patrick Dyer pddyer21@bu.edu

mass_earth=float(5.972e27) 		 #unit:g
neu_add_pro=mass_earth*6.02e23   #the whole number of neu and pro
EperP1=0.5			 #E per P means electron per particle
EperP2=0.4
EperP3=1

a1=neu_add_pro*EperP1		#how much bits
a2=neu_add_pro*EperP2
a3=neu_add_pro*EperP3


print(a1/2**43)
print(a2/2**43)
print(a3/2**43)

