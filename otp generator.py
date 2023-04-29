import random
import string
a=string.ascii_lowercase
n=string.digits
sum=a+n
x=random.choices(sum,k=6)
out=''
for i in x:
    out=out+i 
print("your OTP is:",out)
print("Please do not share this password with anyone.")
    