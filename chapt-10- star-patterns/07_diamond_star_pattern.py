''' 
   *
  ***
 *****
*******
 *****
  ***
   *
'''

n = int(input("Enter number: "))

# Upper part
for i in range(1, n+1):
    spaces = n - i
    stars = 2*i - 1
    
    print(" " * spaces + "*" * stars)

# Lower part
for i in range(n-1, 0, -1):
    spaces = n - i
    stars = 2*i - 1
    
    print(" " * spaces + "*" * stars)