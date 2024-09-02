pre='A'
nex='B'
num=int(input("Enter term : "))
print(pre,"",nex,end=" ")
for i in range(1,num):
   c=nex+pre
   print(c,end=" ")
   pre=nex
   nex=c