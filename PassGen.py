import passwordmeter
import random

LOWERCASE_ASCI = list(range(97, 123))
UPERCASE_ASCI = list(range(65, 91))
NUMBERS_ASCI = list(range(48, 58))
SPECIAL_ASCI = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))


def charGen(charList, passsword):
    no_use = set()
    while len(no_use) < 5:
        no_use.add(random.choice(charList))
    toChose = set(charList) - set(no_use)
    ch = random.sample(toChose, 1)
    while chr(ch[0]) in passsword:
        ch = random.sample(toChose, 1)
    return chr(ch[0])


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


def isInT(options, T):
    check = []
    for ch in options:
        print(ch)
        if ch in T:
            check.append(ch)
    return check


def main():
    while (1):
        print("Choose options; write them separated with spaces")
        options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        # check =  [ch for ch in options if ch in ["A", "L", "U", "N", "S"]]  # ToDo Why this dos not work?
        while not isInT(options, ["A", "L", "U", "N", "S"]):
            print("Entered wrong option ", *options)
            options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        # print("Your options: ", *check)
        howLong = None
        while True:
            try:
                howLong = int(input("Enter lenght: "))
                break
            except Exception as e:
                print("Lenght can be ONLY a digit!")
                # print("\nLenght: " + howLong)
        password = generate(options, howLong)
        strenght, impro = passwordmeter.test(password)
        count = 0
        while strenght < 0.7:
            if count > 100:
                break
            print(strenght)
            print(password)
            password = generate(options, howLong)
            strenght, impro = passwordmeter.test(password)
            count += 1
        print("\n\nGenerated password: " + password)

        print(strenght)
        whatToDo = input("Do you wana exit?[y/n] ")
        if whatToDo == "y":
            break


if __name__ == "__main__":
    main()
