import random


def generate(options, lenght):
    password = ""
    if "A" in options:

        return password
    return None

def main():
    while(1):
        print("Choose options; write them separated with spaces")
        options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        print("Your options: ", *options)
        howLong = None
        while True:
            try:
                howLong = int(input("How long?"))
                break
            except Exception as e:
                howLong = input("Lenght can be ONLY a digit! Enter lenght")
                print("\nLenght: " + howLong)
        password = generate(options, howLong)

        whatToDo = input("Do you wana exit?[y/n]")
        if whatToDo == "y":
            break

main()
