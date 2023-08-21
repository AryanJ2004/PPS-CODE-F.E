class database(): #class 
              mark=[] #  Data Member
              def __init__(self):
                            print("Object is created")
              
              def mark_entry(self,seat_no): # Member function
                            self.seat_no=seat_no
                            self.mark.append(self.seat_no)
                            for i in range(4):
                                          temp=int(input("Subject marks: "))
                                          self.mark.append(temp)

              def display(self): # Member function
                            print("Student Marksheet")
                            print("Seat Number : ",self.mark[0])
                            print("Subject 1 : ",self.mark[1])
                            print("Subject 2 : ",self.mark[2])
                            print("Subject 3 : ",self.mark[3])
                            print("Subject 4 : ",self.mark[4])
                            
              def __del__(self):
                            print("Object is Deleted")

obj1=database() # object creation 
obj1.mark_entry(6985) # method calling using parameter 
obj1.display() # method calling
del obj1
