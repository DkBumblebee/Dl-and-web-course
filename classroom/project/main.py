import csv
import random

def find_user(username, password):
    """
    Find and authenticate user by username and password
    Returns user data if found, None otherwise
    """
    #Error in line 11, 34
    try:
        with open('bank.csv', 'w', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    return row
        return None
    except FileNotFoundError:
        print("Bank database not found!")
        return None

def get_all_users():
    """
    Get all users from the bank.csv file
    Returns liSpam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spamst of user dictionaries
    """
    users = []
    try:
        with open('bank.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)
    except FileNotFoundError:
        print("Bank database note found!")
    return users

def add_new_user(username, password, name, surname, balance, monthly_income="", expenses=""):
    """
    Add a new user to the bank.csv file
    Returns True if successful, False otherwise
    """
    try:
        # Check if file exists and get existing data
        users = get_all_users()
        
        # Create new user data
        new_user = {
            'username': username,
            'password': password,
            'name': name,
            'surname': surname,
            'balance': balance,
            'monthly_income': monthly_income,
            'expenses': expenses
        }
        
        users.append(new_user)
        
        # Write all users back to file
        with open('bank.csv', 'w', newline='') as file:
            fieldnames = ['username', 'password', 'name', 'surname', 'balance', 'monthly_income', 'expenses']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(users)
        
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False

def update_bank_data():
    """
    Updates the bank.csv file with random monthly income and expenses
    """
    # Read the existing data
    users = []
    with open('bank.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    
    # Update each user with random income and expenses
    for user in users:
        # Generate random monthly income
        if user['username'] == 'user009':  # Chris Anderson gets 3x max
            monthly_income = random.randint(1800 * 3, 111000 * 3)  # 5400 to 333000
        else:
            monthly_income = random.randint(1800, 111000)  # 1800 to 111000
        
        # Generate random expenses (should not exceed monthly income)
        # Using 70-95% of income to make it realistic
        expense_percentage = random.uniform(0.70, 0.95)
        expenses = round(monthly_income * expense_percentage, 2)
        
        # Update the user data
        user['monthly_income'] = monthly_income
        user['expenses'] = expenses
        
        # Display the updated info
        print(f"{user['name']} {user['surname']}: Income=${monthly_income:,}, Expenses=${expenses:,}")
    
    # Write the updated data back to the CSV file
    with open('bank.csv', 'w', newline='') as file:
        fieldnames = ['username', 'password', 'name', 'surname', 'balance', 'monthly_income', 'expenses']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(users)
    
    print("\nBank data updated successfully!")


# The below is to test main.py
'''
The Functions below are to test out if what we are doing is correct
'''


def display_all_users():
    """
    Display all users' information from the bank.csv file
    """
    print("\n=== BANK USER INFORMATION ===")
    with open('bank.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"User: {row['name']} {row['surname']}")
            print(f"  Username: {row['username']}")
            print(f"  Balance: ${float(row['balance']):,.2f}")
            if row['monthly_income']:  # Only show if data exists
                print(f"  Monthly Income: ${float(row['monthly_income']):,.2f}")
                print(f"  Monthly Expenses: ${float(row['expenses']):,.2f}")
                savings = float(row['monthly_income']) - float(row['expenses'])
                print(f"  Monthly Savings: ${savings:,.2f}")
            print("-" * 40)

def main():
    """
    Main function to run the banking program
    """
    print("Welcome to the Simple Banking System!")
    print("1. Update random income and expenses")
    print("2. Display all user information")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            update_bank_data()
        elif choice == '2':
            display_all_users()
        elif choice == '3':
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()