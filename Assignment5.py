ilist=[]
even_list=[]
odd_list=[]
for i in range(10):
    temp=int(input("Enter the list value: "))
    ilist.append(temp)
print("Entered List: ",ilist)

for i in ilist:
    if (i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even List: ",even_list)
print("Odd List: ",odd_list)
