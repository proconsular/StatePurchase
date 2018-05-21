from . import Roll

class State:
    name = ""
    siblings = []
    GDP = 0.0
    tax = 0.1
    money = 10.0
    population = 0.0
    crime = 0.1
    police = 1

    def __init__(self, name, population):
        self.name = name
        self.population = population
        GDP = population * 70

    def process(self):
        if Roll.chance(0.5):
            self.population *= 1.1
        self.GDP *= 1 + self.population * random.uniform(0, 10) * 0.01
        self.money += self.computeIncome()

    def computeIncome(self):
        return self.GDP * self.tax

    def computeExpenses(self):
        return population * crime * 5
