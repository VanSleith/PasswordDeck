import random


class PassGenerator:
    length = None

    def __init__(self, length):
        self.length = length

    def setLength(self, length):
        self.length = length

    def charGen(self, charList, passsword):
        no_use = set()
        while len(no_use) < 5:
            no_use.add(random.choice(charList))
        toChose = set(charList) - set(no_use)
        ch = random.sample(toChose, 1)
        while chr(ch[0]) in passsword:
            ch = random.sample(toChose, 1)  # ToDo Find if it's better than allowing same characters
        return chr(ch[0])

    def passGen(self, charList):
        password = ""
        while len(password) < self.length:
            password = password + self.charGen(charList, password)
        return password

    def generate(self, options):
        characters = []
        if "A" in options:
            characters = list(range(33, 125))
            return self.passGen(characters)

        if "L" in options:
            characters = characters + list(range(97, 123))
        if "U" in options:
            characters = characters + list(range(65, 91))
        if "N" in options:
            characters = characters + list(range(48, 58))
        if "S" in options:
            characters = characters + list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(
                range(123, 127))
        if not characters:
            raise NotImplemented
        return self.passGen(characters)

    # def __str__(self):
    #     return self.generate("A")

    def __repr__(self):
        return self.generate("A")
