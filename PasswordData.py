from PassGen import PassGenerator


class Password():

    def __init__(self, name="", machine_ip="", password=PassGenerator(8)):
        self.name = name
        self.machine_ip = machine_ip
        self.password = password

    def __str__(self):
        return "Acces to {} by {} under a name: {}".format(self.machine_ip, str(self.password), self.name)


if __name__ == "__main__":
    print(Password("First", "10.10.10.10"))
