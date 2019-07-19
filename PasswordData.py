from PassGen import PassGenerator


class Password():

    def __init__(self, name="", password=PassGenerator(8)):
        self.name = name
        self.password = password

    def __str__(self):
        return "Access by {} under a name: \"{}\"".format(str(self.password), self.name)


class SerwerPassword(Password):
    def __init__(self, name="", machine_ip=""):
        super().__init__(name)
        self.machine_ip = machine_ip

    def __str__(self):
        return super().__str__() + " to machine under ip: {}".format(self.machine_ip)


if __name__ == "__main__":
    print(Password("First"))
    print(SerwerPassword("Second", "10.10.10.10"))
