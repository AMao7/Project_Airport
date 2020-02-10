class People():
    def __init__(self, name):
        self.name = name

class Passenger(people):
    def __init__(self, __passport):
        self.__passport = __passport