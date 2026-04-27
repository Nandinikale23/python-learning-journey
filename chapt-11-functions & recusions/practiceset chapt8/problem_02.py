# WAP using function to convert celsius to fahrenheit.



def f_to_c(f):
    return 5*(f-32)/9

f= int(input("ener temp in f: "))
print(f"{f_to_c(f)}°C")