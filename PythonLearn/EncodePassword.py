import hashlib
import os

#user = name, password
#testing the hashing algorithm
password = "123456"
salt = os.urandom(32)

key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,1000)

print(key)

password_entered = '123456'
key_check = hashlib.pbkdf2_hmac('sha256', password_entered.encode('utf-8'),salt,1000)

if key_check == key:
    print("The password is correct")
else:
    print("The password is wrong")
