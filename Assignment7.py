def menu():
    print("\nMenu\n\n 1. Calculate length of string\n 2. String reversal\n 3. Equality check of two strings\n 4. Check palindrome\n 5. Check substring\n 6. Exit\n")
    option=int(input("Enter your option: "))
    return option

def reversal(str1):
    print("\nString reversal\n")
    for i in range(len(str1)-1,-1,-1):
        print(str1[i],end="")

def equality(str1,str2):
    if str1==str2:
        print("Sting are equal ",)
    else:
        print("Sting are NOT equal ",)

def palindrome(str1):
    str2=""
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    if str1 == str2:
        print("String is Palindrome")
    else:
        print("String is NOT Palindrome")

def substring(str1,str2):
    if str2 in str1:
        print("Sting 2 is substring String 1  ",)
    else:
        print("Sting 2 is not substring String 1  ",)

#Main program
option=menu()
if (option==1):
    str1=input("Enter the String 1  : ")
    print("Length of sting 1 ", len(str1))
elif (option==2):
    str1=input("Enter the String 1  : ")
    reversal(str1)
elif (option==3):
    str1=input("Enter the String 1  : ")
    str2=input("Enter the String 2  : ")
    equality(str1,str2)
elif (option==4):
    str1=input("Enter the String 1  : ")
    palindrome(str1)
elif (option==5):
    str1=input("Enter the String 1  : ")
    str2=input("Enter the String 2  : ")
    substring(str1,str2)
elif (option==6):
    exit     
else:
    print("You have entered wrong option...")
