'''spam comment is defined as a text containing following keywords: "make a lot of money","buy now","subscribe this","click this".
WAP to detect these spam'''

comment1="make a lot of money"
comment2="buy now"
comment3="subcribe this"
comment4="click this"

comment=input("enter comment to detect spam:")


if((comment1 in comment) or (comment2 in comment) or (comment3 in comment) or (comment4 in comment )):
    print("this comment is a spam ")
else:
    print("this comment is not spam")