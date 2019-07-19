import passwordmeter

from PassGen import PassGenerator


class Main:
    options = None
    length = None
    password = None
    strength = None
    generator = PassGenerator(10)

    def __init__(self):
        pass

    def setPassOptions(self):
        print("Choose options; write them separated with spaces")
        self.options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        check = [ch for ch in self.options if ch in ["A", "L", "U", "N", "S"]]
        while not check:
            print("Entered wrong option ", *self.options)
            self.options = input("(A)ll-or- (L)owercase, (U)percase,(N)umbers, (S)pecjal ").split()
        # print("Your options: ", *check)

    def setLenght(self):
        while True:
            try:
                self.length = int(input("Enter length: "))
                self.generator.set_length(self.length)
                break
            except Exception as e:
                print("Length can be ONLY a digit!")
                # print("\nLength: " + self.length)

    def generate(self):
        self.password = self.generator.generate(self.options)
        self.strength, impro = passwordmeter.test(self.password)
        count = 0
        while self.strength < 0.7:
            if count > 100:
                break
            self.password = self.generator.generate(self.options)
            self.strength, impro = passwordmeter.test(self.password)
            count += 1

    def mainLoop(self):
        while True:
            self.setPassOptions()
            self.setLenght()
            self.generate()
            print("\n\nGenerated password: " + self.password)

            print(self.strength)
            whatToDo = input("Do you want to exit?[y/n] ")
            if whatToDo == "y":
                break


if __name__ == "__main__":
    Main().mainLoop()
