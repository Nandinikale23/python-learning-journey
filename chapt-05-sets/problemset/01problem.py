'''WAP to find out wethear student is passed or failed if its required total 40% and at least 33% in each subject to paased.
assume 3 subjects and take marks as an input from user'''

marks1=int(input("enter marks of subject1:"))
marks2=int(input("enter marks of subject2:"))
marks3=int(input("enter marks of subject3:"))

total_percentage=(100*(marks1+marks2+marks3))/300
print(total_percentage)

if(total_percentage>40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("student is passed and your percentage is:",total_percentage)
else:
    print("student is failed and your percentage is :",total_percentage)