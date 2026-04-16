class planet:
    whatsr = None
    id = 0

    def __init__(self, name, radius, weight, distanceFromTheSun, type):
        self.id = planet.id
        self.name = name
        self.radius= radius
        self.weight = weight
        self.distanceFromTheSun = distanceFromTheSun
        self.type = type
        print(f"создан обект ID: {self.id}")
        planet.id += 1

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
            print("ff")
            return self.radius <= other.radius
        if planet.whatsr == "Масса" or planet.whatsr == "weight":
            return self.weight <= other.weight
        if planet.whatsr == "Расстояние от Солнца" or planet.whatsr == "distance from the Sun":
            return self.distanceFromTheSun <= other.distanceFromTheSun
        if planet.whatsr == "Тип" or planet.whatsr == "type":
            return self.type <= other.type
        return None
    
    def getDataList(self):
        return [self.name, self.radius, self.weight, self.distanceFromTheSun, self.type, self.id]
    
    @classmethod
    def create(cls, data):
        if len(data) == 5:
            return cls(data[0], data[1], data[2], data[3], data[4])
        return None
