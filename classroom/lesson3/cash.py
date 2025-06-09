from main import get_int

def main():
    change = coin()
    print(f"Change owed: {change}")

def coin():
    while True:
        c = float(input("Change:"))
        if c > 0:
            break
    coins = round(c * 100)
    num = 0
    while coins > 0:
        if coins >= 25:
            coins -= 25
            num +=1
        elif coins >= 10:
            coins -= 10
            num += 1
        elif coins >= 5:
            coins -= 5
            num += 1
        else:
            coins -= 1
            num +=1
    return num
main()