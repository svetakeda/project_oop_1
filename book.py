class Book:
    def __init__(self, name, year, author, cost):
        self.__name = name
        self.__year = year
        self.__author = author
        self.__cost = cost

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def author(self):
        return self.__author

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    def __str__(self):
        return f"{self.__name} {self.__year} {self.__author} {self.__cost}"

    def __repr__(self):
        return f"{self.__name} {self.__year} {self.__author} {self.__cost}"
