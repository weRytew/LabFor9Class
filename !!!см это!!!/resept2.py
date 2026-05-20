class resept:
    whatsr = None
    id = 0

    def __init__(self, name, categoray, timeForCook, ingredients, level):
        self.__id = resept.id
        self.name = name
        self.categoray= categoray
        self.__timeForCook = timeForCook
        self.__ingredients = ingredients
        self.level = level
        print(f"создан обект ID: {self.id}")
        resept.id += 1

    @property
    def timeForCook(self):
        return self.__timeForCook

    @timeForCook.setter
    def timeForCook(self, timeForCook):
        if type(timeForCook) == int:
            if int(timeForCook) > 0:
                self.__timeForCook = timeForCook
        else:
            print("некоректоно")

    def __str__(self):
        return (f"имя: {self.name }\n"
                f"категория: {self.categoray}\n"
                f"время приготовления: {self.timeForCook}\n"
                f"ингредиенты: {self.__ingredients}\n"
                f"сложность: {self.level}\n")
    
    def __repr__(self):
        return f"имя: {self.name }\n" + f"категория: {self.categoray}\n" + f"время приготовления: {self.timeForCook}\n" + f"ингредиенты: {self.__ingredients}\n" + f"сложность: {self.level}\n"
    
    def __copy__(self):
        new = resept(self.name, self.categoray, self.timeForCook, self.__ingredients, self.level)
        return new
    
    def __del__(self):
        print(f"{self.id} удаелн")
    
    def __lt__(self, other):
        return self.__timeForCook < other.__timeForCook

    def __eq__(self, other):
        return self.name ==  other.name

    def __le__(self, other):
        if resept.whatsr == "name":
            return self.name <= other.name
        if resept.whatsr == "categoray":
            return self.categoray <= other.categoray
        if resept.whatsr == "timeForCook":
            return self.__timeForCook <= other.__timeForCook
        if resept.whatsr == "ingredients":
            return self.__ingredients <= other.__ingredients
        if resept.whatsr == "level":
            return self.level <= other.level
        return None
    
    def getDataList(self):
        return [self.name, self.categoray, self.timeForCook, self.__ingredients, self.level, self.__id]
    
    @classmethod
    def create(cls, data):
        if len(data) == 5:
            try:
                return cls(data[0], data[1], int(data[2]), data[3], data[4])
            except:
                print("некоректные данные")
        return None