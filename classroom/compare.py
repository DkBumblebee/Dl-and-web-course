username = "bumblebee"
user_password = "password123"
balance = 1300

name = input("What is your username: ").lower()
password = input("What is your password: ")


if (name == username) and (password == user_password):
    print("Welcome")
else:
    print("Goodbye")