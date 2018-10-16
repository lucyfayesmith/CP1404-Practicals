class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        guitar_age = 2018 - self.year
        return guitar_age

    def is_vintage(self):
        return self.get_age() >= 50