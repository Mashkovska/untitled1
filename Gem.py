class Gem:
    comparing_number = 0
    change_number = 0

    @staticmethod
    def compare_count():
        Gem.comparing_number += 1
        return Gem.comparing_number

    @staticmethod
    def change_count():
        Gem.change_number += 1
        return Gem.change_number

    @staticmethod
    def reset_count():
        Gem.comparing_number = 0
        Gem.change_number = 0

    def __init__(self, name, count_punish, price):
        self.name = name
        self.count_punish = count_punish
        self.price = price

    def __repr__(self):
        return str(self.name) + " " + str(self.count_punish) + " " + str(self.price)


