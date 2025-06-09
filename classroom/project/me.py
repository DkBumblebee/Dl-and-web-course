while True:
    try:
        balance = float(input("Enter initial deposit amount: R"))
        if balance < 0:
            print("Initial deposit cannot be negative!")
            continue
        break
    except ValueError:
        print("Please enter a valid amount!")
        pass

print(f"R{balance:,.2f}")