import random
import string

chars = string.ascii_letters + string.digits + "!@#$%"
length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)