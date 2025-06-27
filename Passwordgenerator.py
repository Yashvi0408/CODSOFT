import random
import string

#Get all the characters
characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

#Request for length
length = int(input("Enter the password lengt: "))

#Create password
password = ''.join(random.choices(characters, k=length))

#Print password
print("Password:", password)