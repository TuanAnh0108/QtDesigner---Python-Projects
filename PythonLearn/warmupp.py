import myLib

cities = [(3,5), (9,10),(7,8),(15,7)]
nameOfCity = ["A", "B", "C", "D"]
length = len(cities)

for i in range(4):
    cityA = cities[i]
    for i2 in range(i+1,4):
        cityB = cities[i2]
        distances = (myLib.distance(target = cityB, origin = cityA))
        print("Distance between city {} and {} is {}".format(nameOfCity[i],nameOfCity[i2],distances))

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
