ec=int(input("Enter the EC marks: "))
em1=int(input("Enter the EM1 marks: "))
sme=int(input("Enter the SME marks: "))
pps=int(input("Enter the PPS marks: "))
bee=int(input("Enter the BEE marks: "))
total=ec+em1+sme+pps+bee
agg=total/5
grade="null"

if (ec>=40 and em1>=40 and sme>=40 and pps>=40 and bee>=40):
              result="Pass"
              if (agg>=75):
                            grade="Distinction"
              elif(agg>=60 and agg<75):
                            grade="First class"
              elif(agg>=50 and agg<60):
                            grade="Second class"
              elif(agg>=40 and agg<50):
                            grade="Third class"
else:
              result="Fail"
print("Result: ",result)
print("Total: ",total)
print("Aggreget: ",agg)
print("Grade: ",grade)





