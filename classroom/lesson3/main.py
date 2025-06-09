def main():
    print("My function") 

       
def get_height():
    while True:
        n = get_int("Heigth: ")
        if n > 0 and n < 10:
            return n

    

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue

if __name__ == "__main__":
    main()