import random

LOWERCASE_ASCI = list(range(97, 123))
UPERCASE_ASCI = list(range(65, 91))
NUMBERS_ASCI = list(range(48, 58))
SPECIAL_ASCI = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))


def charGen(charList, passsword):
    ch = random.choice(charList)
    while chr(ch) in passsword:
        ch = random.choice(charList)
    return chr(ch)


def passGen(lenght, charList):
    password = ""
    while len(password) < lenght:
        password = password + charGen(charList, password)
    return password


def generate(options, lenght):
    characters = []
    if "A" in options:
        characters = list(range(33, 125))
        return passGen(lenght, characters)

    if "L" in options:
        characters = characters + LOWERCASE_ASCI
    if "U" in options:
        characters = characters + UPERCASE_ASCI
    if "N" in options:
        characters = characters + NUMBERS_ASCI
    if "S" in options:
        characters = characters + SPECIAL_ASCI
    if not characters:
        raise NotImplemented
    return passGen(lenght, characters)


def main():
    while (1):
        print("Choose options; write them separated with spaces")
        options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        check = [ch for ch in options if ch in ["A", "L", "U", "N", "S"]]  # ToDo Right options checking algorithm
        while not check:
            print("Entered wrong option ", *options)
            options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        print("Your options: ", *options)
        howLong = None
        while True:
            try:
                howLong = int(input("How long? "))
                break
            except Exception as e:
                howLong = input("Lenght can be ONLY a digit! Enter lenght")
                # print("\nLenght: " + howLong)
        password = generate(options, howLong)
        print("\n\nGenerated password: " + password)
        whatToDo = input("Do you wana exit?[y/n] ")
        if whatToDo == "y":
            break


main()
