import passwordmeter

from PassGen import PassGenerator


def isInT(A, T):
    check = []
    for ch in A:
        print(ch)
        if ch in T:
            check.append(ch)
    return check


class Main:
    options = None
    length = None
    password = None
    strenght = None
    generator = None

    def __init__(self):
        pass

    def setPassOptions(self):
        print("Choose options; write them separated with spaces")
        self.options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        # check =  [ch for ch in options if ch in ["A", "L", "U", "N", "S"]]  # ToDo Why this dos not work?
        while not isInT(self.options, ["A", "L", "U", "N", "S"]):
            print("Entered wrong option ", *self.options)
            self.options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        # print("Your options: ", *check)

    def setLenght(self):
        while True:
            try:
                self.length = int(input("Enter length: "))
                self.generator = PassGenerator(self.length)
                break
            except Exception as e:
                print("Lenght can be ONLY a digit!")
                # print("\nLenght: " + self.lenght)

    def generate(self):
        self.password = self.generator.generate(self.options)
        self.strenght, impro = passwordmeter.test(self.password)
        count = 0
        while self.strenght < 0.7:
            if count > 100:
                break
            self.password = self.generator.generate(self.options)
            self.strenght, impro = passwordmeter.test(self.password)
            count += 1

    def mainLoop(self):
        while True:
            self.setPassOptions()
            self.setLenght()
            self.generate()
            print("\n\nGenerated password: " + self.password)

            print(self.strenght)
            whatToDo = input("Do you wana exit?[y/n] ")
            if whatToDo == "y":
                break


if __name__ == "__main__":
    Main().mainLoop()
