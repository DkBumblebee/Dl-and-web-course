def main():
    scores = get_int("Scores: ")
    print(f"You got {scores} out of 50")
    x = (scores / 50) * 100
    print(f"You got {x}%")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue

main()