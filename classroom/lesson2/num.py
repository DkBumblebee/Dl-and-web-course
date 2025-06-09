def main():
    while True:
        try:
            num = int(input("What is x? "))
            print(f"X equals {num}")
            break
        except ValueError:
            print(f"X is not an int")
            continue
        
main()