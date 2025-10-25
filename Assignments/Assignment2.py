import sys

username = "Admin"
password = "1234"
attempts = 3

for attempt in range(attempts):
    enter_username = input("Enter your username : ")
    enter_password = input("Enter your password : ")

    if enter_username == username and enter_password == password:
        print("Access Granted")
        break
    elif attempt == 2:
        sys.exit("Acount locked")
    else:
        print("wrong username or password, please repeat(you only have 3 attempts) ")
number = int(input("Enter a number. All prime numbers between 2 and that number will be displayed : "))

for i in range(2, number):
    n = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            n = False
    if n == True:
        print(f"Prime number = {i}")
