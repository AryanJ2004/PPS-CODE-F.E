num=int(input("Enter the number: ")) 
num1=num
sum=0
unit=0

while (num>0):
          unit=num%10 
          num=num//10
          sum=sum+(unit**3)
if (sum==num1):
          print("Number is Armstrong number")
else:
          print("Number is not Armstrong number")
          
