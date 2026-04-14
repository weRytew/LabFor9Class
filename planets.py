class planet:
    whatsr = None

    def __init__(self, name, radius, weight, distanceFromTheSun, type):
        self.name = name
        self.radius= radius
        self.weight = weight
        self.distanceFromTheSun = distanceFromTheSun
        self.type = type

    def __str__(self):
        return (f"имя: {self.name }\n"
                f"радиус: {self.radius}\n"
                f"масса: {self.weight}\n"
                f"расстояние от Солнца: {self.distanceFromTheSun}\n"
                f"тип: {self.type}")
    
    def __le__(self, other):
        if planet.whatsr == "имя" or planet.whatsr == "name":
            return self.name < other.name
        if planet.whatsr == "Радиус" or planet.whatsr == "radius":
            return self.radius < other.radius
        if planet.whatsr == "Масса" or planet.whatsr == "weight":
            return self.weight < other.weight
        if planet.whatsr == "Расстояние от Солнца" or planet.whatsr == "distance from the Sun":
            return self.distanceFromTheSun < other.distanceFromTheSun
        if planet.whatsr == "Тип" or planet.whatsr == "type":
            return self.type < other.type
        return None
    
    def getDataList(self):
        return [self.name, self.radius, self.weight, self.distanceFromTheSun, self.type]
    
    @classmethod
    def create(cls, data):
        if len(data) == 5:
            return cls(data[0], data[1], data[2], data[3], data[4])
        return None