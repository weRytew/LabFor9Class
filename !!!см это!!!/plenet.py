class planet:
    whatsr = None
    id = 0

    def __init__(self, name, radius, weight, distanceFromTheSun, type1):
        if type(radius) == int and type(weight) == int and type(distanceFromTheSun) == int:
            if radius > 0 and weight > 0 and distanceFromTheSun > 0:
                self.__id = planet.id
                self.name = name
                self.__radius = radius
                self.__weight = weight
                self.__distanceFromTheSun = distanceFromTheSun
                self.type = type1
                print(f"создан обект ID: {self.id}")
                planet.id += 1
            else:
                self.__del__()
        else:
            self.__del__()

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, newRadius):
        if type(newRadius) == int:
            if int(newRadius) > 0:
                self.__radius = newRadius
        else:
            print("некоректоно")

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, newWeight):
        if type(newWeight) == int:
            if int(newWeight) > 0:
                self.__weight = newWeight
        else:
            print("некоректоно")
    
    @property
    def distanceFromTheSun(self):
        return self.__distanceFromTheSun
    
    @distanceFromTheSun.setter
    def distanceFromTheSun(self, newDistanceFromTheSun):
        if type(newDistanceFromTheSun) == int:
            if int(newDistanceFromTheSun) > 0:
                self.__distanceFromTheSun = newDistanceFromTheSun
        else:
            print("некоректоно")

    def __str__(self):
        return (f"имя: {self.name }\n"
                f"радиус: {self.radius}\n"
                f"масса: {self.weight}\n"
                f"расстояние от Солнца: {self.distanceFromTheSun}\n"
                f"тип: {self.type}\n")
    
    def __repr__(self):
        return f"имя: {self.name} радиус: {self.radius} вес: {self.weight} растояние от солнца: {self.distanceFromTheSun} тип: {self.type}"
    
    def __copy__(self):
        new = planet(self.name, self.radius, self.weight, self.distanceFromTheSun, self.type)
        return new
    
    def __del__(self):
        print(f"{self.id} удаелн")
    
    def __lt__(self, other):
        return self.distanceFromTheSun < other.distanceFromTheSun

    def __eq__(self, other):
        return self.name ==  other.name

    def __le__(self, other):
        if planet.whatsr == "имя" or planet.whatsr == "name":
            return self.name <= other.name
        if planet.whatsr == "Радиус" or planet.whatsr == "radius":
            return self.__radius <= other.__radius
        if planet.whatsr == "Масса" or planet.whatsr == "weight":
            return self.__weight <= other.__weight
        if planet.whatsr == "Расстояние от Солнца" or planet.whatsr == "distance from the Sun":
            return self.__distanceFromTheSun <= other.__distanceFromTheSun
        if planet.whatsr == "Тип" or planet.whatsr == "type":
            return self.type <= other.type
        return None
    
    def getDataList(self):
        return [self.name, self.radius, self.weight, self.distanceFromTheSun, self.type, self.id]
    
    @classmethod
    def create(cls, data):
        if len(data) == 5:
            try:
                return cls(data[0], int(data[1]), int(data[2]), int(data[3]), data[4])
            except:
                print("некоректные данные")
        return None