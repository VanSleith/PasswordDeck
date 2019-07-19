import random


class PassGenerator:
    length = None

    def __init__(self, length):
        self.length = length

    def set_length(self, length):
        self.length = length

    def char_gen(self, charList):
        no_use = set()
        while len(no_use) < 5:
            no_use.add(random.choice(charList))
        toChose = list(set(charList) - set(no_use))

        for i in range(self.length):
            ch = random.sample(toChose, 1)
            toChose.remove(ch[0])
            yield chr(ch[0])

    def pass_gen(self, charList):
        password = ""
        c = self.char_gen(charList)
        for char in c:
            password = password + char
        return password

    def generate(self, options):
        options = options.upper()
        characters = []
        if "A" in options:
            characters = range(33, 125)
            return self.pass_gen(characters)

        if "L" in options:
            characters.extend(range(97, 123))
        if "U" in options:
            characters.extend(range(65, 91))
        if "N" in options:
            characters.extend(range(48, 58))
        if "S" in options:
            characters.extend(range(33, 48) + range(58, 65) + range(91, 97) +
                              range(123, 127))
        if not characters:
            raise NotImplemented
        return self.pass_gen(characters)

    # def __str__(self):
    #     return self.generate("A")

    def __repr__(self):
        return self.generate("A")


if __name__ == "__main__":
    print(PassGenerator(8).generate("a"))  # input("Insert options for password[A,L,U,N,S]")))
