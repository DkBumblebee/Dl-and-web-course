import csv

def main():
    """
    Main Banking system menu
    """

    print("=" * 60)
    print("           WECOME TO IMENTORU BANKING SYSTEM")
    print("=" * 60)

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using IMENTORU Bank!")
            break
        else:
            print("Invalid choice. Please try again.")

      
    #user = login()
    #print(f"Welcome {user}")

def login():
    name = input("What is your username: ")
    password = input("What is your password: ")

    user = find_user(name, password)[1]
    username= user[0]
    user_password = user[-2]

    if (name == username) and (password == user_password):
        print(f"Welcome {name}")
        return name
    else:
        print("Username or password is incorrect")

def register():
    name = input("Enter your first name: ").strip()
    surname = input("Enter your surname: ").strip()

    username = f"user{+ 1:03}"
    password = input("Create a passwordword (7-12 characters): ").strip()
    if len(password) < 7 or len(password) > 12:
        print("\nPassword must be between 7-12 characters!")
        return

    # Initial Balance
    while True:
        try:
            balance = float(input("Enter initial deposit ammount: R"))
            if balance < 0:
                print("Initial deposit cannot be negative!")
                return
            else:
                break
        except ValueError:
            print("Please enter a valid amount")
            return
    user_data = [name, surname, username, password, balance]
    if user_data:
        with open('bank.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(user_data)
    return


def find_user(name, password):
    # TODO
    
    return user_data
            
main()