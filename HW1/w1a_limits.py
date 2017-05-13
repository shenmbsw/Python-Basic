# AUTHOR ShenShen shs2016f@bu.edu

Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
print(Table.format(1,2**8-1,-(2**7),2**7-1))
print(Table.format(2,2**16-1,-(2**15),2**15-1))
print(Table.format(4,2**32-1,-(2**31),2**31-1))
print(Table.format(8,2**64-1,-(2**63),2**63-1))
