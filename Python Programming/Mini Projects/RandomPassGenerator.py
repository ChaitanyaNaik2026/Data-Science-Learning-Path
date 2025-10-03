import random
import string

userChoice = int(input("Enteer the length of password :"))
#pass_len =12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(userChoice):
   password += (random.choice(charValues))
print("YOur random password is:",password)

#to get each char in list use list compression
#to concatenate string use .join

password2 = "".join([random.choice(charValues) for i in range(userChoice)])
print(password2)