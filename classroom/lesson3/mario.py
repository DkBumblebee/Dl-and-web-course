def main():
    height = get_height()
    for i in range(height):
        for j in range(height):
            if j >= i+1:
                print(" ", end="")
            else:
                print("#", end="")
        print()
        
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
main()
