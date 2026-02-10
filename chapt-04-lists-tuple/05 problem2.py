#WAP to accept marks of 6 marks and display them in sorted manner 
students=[]
s1=int(input("enter marks of student s1:"))
students.append(s1)
s2=int(input("enter marks of student s2:"))
students.append(s2)
s3=int(input("enter marks of student s3:"))
students.append(s3)
s4=int(input("enter marks of student s4:"))
students.append(s4)
s5=int(input("enter marks of student s5:"))
students.append(s5)
s6=int(input("enter marks of student s6:"))
students.append(s6)

students.sort()
print(students)