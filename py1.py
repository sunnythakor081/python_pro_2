no=int(input("enter number"))
number=[]
sum1=0
for i in range(1,no):
    if(no%i==0):
        number.append(i)
print(number)
for i in number:
    sum1=sum1+i
    #print(i)
if(no==sum1):
  print("Number is perfect..")
else:
    print("Number is not perfect..")