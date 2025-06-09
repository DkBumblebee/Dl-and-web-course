import csv
from main import find_user, get_all_users, add_new_user

# Global variable to store current logged-in user
current_user = None

def main():
    """
    Main banking system menu
    """
    print("="*50)
    print("    WELCOME TO SIMPLE BANKING SYSTEM")
    print("="*50)
    
    while True:
        print("\n1. Register New Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

def register():
    """
    Register a new user account
    """
    print("\n=== REGISTER NEW ACCOUNT ===")
    
    # Get user details
    name = input("Enter your first name: ").strip()
    surname = input("Enter your surname: ").strip()
    
    # Generate username
    username = f"user{len(get_all_users()) + 1:03d}"
    
    # Get password
    password = input("Create a password (7-25 characters): ").strip()
    
    # Validate password length
    if len(password) < 7 or len(password) > 25:
        print("Password must be between 7-25 characters!")
        return
    
    # Initial balance
    try:
        balance = float(input("Enter initial deposit amount: $"))
        if balance < 0:
            print("Initial deposit cannot be negative!")
            return
    except ValueError:
        print("Please enter a valid amount!")
        return
    
    # Add new user
    if (username, password, add_new_username, surname, balance):
        print(f"\nAccount created successfully!")
        print(f"Your username is: {username}")
        print("You can now login with your credentials.")
    else:
        print("Error creating account. Please try again.")

def login():
    """
    User login system
    """
    global current_user
    
    print("\n=== LOGIN ===")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    user = find_user(username, password)
    
    if user:
        current_user = user
        puser_menurint(f"\nWelcom {user['name']} {user['surname']}!")
        ()
    else:
        print("Invalid username or password!")

def user_menu():
    """
    Menu for logged-in users
    """
    while True:
        print(f"\n=== WELCOME {current_user['name'].upper()} ===")
        print("1. Check Balance")
        print("2. Bank Statement")
        print("3. Logout")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            bank_balance()
        elif choice == '2':
            bank_statement()
        elif choice == '3':
            logout()
            break
        else:
            print("Invalid choice. Please try again.")

def bank_balance():
    """
    Display current user's balance
    """
    print("\n=== ACCOUNT BALANCE ===")
    print(f"Account Holder: {current_user['name']} {current_user['surname']}")
    print(f"Username: {current_user['username']}")
    print(f"Current Balance: ${float(current_user['balance']):,.2f}")

def bank_statement():
    """
    Display user's bank statement with income and expenses
    """
    print("\n=== BANK STATEMENT ===")
    print(f"Account Holder: {current_user['name']} {current_user['surname']}")
    print(f"Username: {current_user['username']}")
    print("-" * 40)
    print(f"Current Balance: ${float(current_user['balance']):,.2f}")
    
    # Check if income/expenses data exists
    if current_user['monthly_income'] and current_user['expenses']:
        monthly_income = float(current_user['monthly_income'])
        expenses = float(current_user['expenses'])
        savings = monthly_income - expenses
        
        print(f"Monthly Income: ${monthly_income:,.2f}")
        print(f"Monthly Expenses: ${expenses:,.2f}")
        print(f"Monthly Savings: ${savings:,.2f}")
        
        # Financial health indicator
        savings_rate = (savings / monthly_income) * 100
        print(f"Savings Rate: {savings_rate:.1f}%")
        
        if savings_rate >= 20:
            print("💚 Excellent savings rate!")
        elif savings_rate >= 10:
            print("💛 Good savings rate!")
        else:
            print("💡 Consider reducing expenses to save more!")
    else:
        print("Monthly income/expenses data not available.")
        print("Please contact admin to update your financial information.")

def logout():
    """
    Logout current user
    """
    global current_user
    print(f"Goodbye, {current_user['name']}!")
    current_user = None

if __name__ == "__main__":
    main()