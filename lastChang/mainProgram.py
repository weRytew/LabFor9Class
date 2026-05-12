import json

from planet import planet
# import planets

howSort = None

def A():
    print()
    # def getAllPlanetsList():
    #     with open("jsonPlanets.json", "r") as jsonWithPlanets:
    #         listPlanetsJson = json.load(jsonWithPlanets)
    #     listPlanets= []
    #     for i in listPlanetsJson:
    #         name = i
    #         radius = listPlanetsJson[i]["radius"]
    #         weight = listPlanetsJson[i]["weight"]
    #         distanceFromTheSun = listPlanetsJson[i]["distanceFromTheSun"]
    #         type = listPlanetsJson[i]["type"]
    #         planet = planets.planet(name, radius, weight,distanceFromTheSun, type)
    #         listPlanets.append(planet)
    #     return listPlanets

    # def getAllPlanetsDict():
    #     with open("jsonPlanets.json", "r") as jsonWithPlanets:
    #         return json.load(jsonWithPlanets)

    # def updateJsonWithPlanets(updateList):
    #     with open("jsonPlanets.json", "w") as jsonWithPlanets:
    #         json.dump(updateList, jsonWithPlanets)

    # # def update(newList):
    # #
    # #     for i in newList

    # def updatePlanet(namePlanet, whatUpdate, value):
    #     planetsDict = getAllPlanetsDict()
    #     try:
    #         if whatUpdate != "name":
    #             planetsDict[namePlanet][whatUpdate] = value
    #         else:
    #             data = planetsDict[namePlanet]
    #             delPlanet(namePlanet)
    #             name = value
    #             radius = data["radius"]
    #             weight = data["weight"]
    #             distanceFromTheSun = data["distanceFromTheSun"]
    #             type = data["type"]
    #             planet = planets.planet(name, radius, weight, distanceFromTheSun, type)
    #             addPlanetInJson(planet)
    #     except:
    #         print("бывает")

    # def delPlanet(namePlanet):
    #     planetsDict = getAllPlanetsDict()
    #     del planetsDict[f"{namePlanet}"]
    #     updateJsonWithPlanets(planetsDict)

    # def addPlanetInJson(planet):
    #     with open("jsonPlanets.json", "r") as jsonWithPlanets:
    #         listPlanets = json.load(jsonWithPlanets)
    #     listPlanets[planet.name] = {"radius": planet.radius,
    #                                 "weight": planet.weight,
    #                                 "distanceFromTheSun": planet.distanceFromTheSun,
    #                                 "type": planet.type}
    #     updateJsonWithPlanets(listPlanets)

    # def ssort(what):
    #     listPlanets = getAllPlanetsList()
    #     for i in range(len(listPlanets)):
    #         indexMinElrmrnt = i
    #         for j in range(i, len(listPlanets)):
    #             if  planets.planet.__le__(listPlanets[indexMinElrmrnt], listPlanets[j], what):
    #                 indexMinElrmrnt = j
    #         listPlanets[i], listPlanets[indexMinElrmrnt] = listPlanets[indexMinElrmrnt], listPlanets[i]
    #     return listPlanets


def read():
    try:
        with open("db.json", "r", encoding="utf-8") as file:
            a = 1
    except:
        with open("db.json", "w", encoding="utf-8") as file:
            print("{}", file=file)
    with open("db.json", "r", encoding="utf-8") as file:
        return json.load(file)

def addElenment(newData: planet):
    lastData = read()
    updatingData = lastData
    updatingData[len(lastData)] = newData.getDataList()
    write(updatingData)

def write(data):
    if type(data) == list:
        data = listToJs(data)
    with open("db.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def listToJs(ls: list[planet]):
    js = {}
    for i in range(len(ls)):
        js[i] = ls[i].getDataList()
    return js

def dictToList(dict):
    conList = []
    for i in dict:
        conList.append(dict[i])
    return conList

def listToDict(array):
    dict = {}
    for i in range(len(array)):
        dict[i] = array[i]
    return dict

def howSortFunc(dataElement):
    global howSort
    if howSort == "имя" or howSort == "name":
        return dataElement[0]
    if howSort == "Радиус" or howSort == "radius":
        return dataElement[1]
    if howSort == "Масса" or howSort == "weight":
        return dataElement[2]
    if howSort == "Расстояние от Солнца" or howSort == "distance from the Sun":
        return dataElement[3]
    if howSort == "Тип" or howSort == "type":
        return dataElement[4]

def sortDB(pole):
    global howSort
    howSort = pole
    planetDiction = read()
    planetList = dictToList(planetDiction)
    planetList.sort(key=howSortFunc)
    dict = listToDict(planetList)
    write(dict)

def pereraschet(dict):
    corectDict = {}
    nowId = 0
    for i in dict:
        corectDict[nowId] = dict[i]
        nowId += 1
    return corectDict

def delElement(index):
    try:
        dict = read()
        dict.pop(str(index-1), None)
        dict = pereraschet(dict)
        write(dict)
    except:
        print("ошибка при удалении")

def chengeElement(index, newElement):
    try:
        if len(newElement) == 5 and type(newElement) == list:
            dict = read()
            dict[index] = newElement
            write(dict)
        else:
            return None
    except:
        print("Ошибка при изменении")
        return None

def maxLen(dict):
    mxId = 1
    mxName = 1
    mxRadius = 1
    mxWeight = 1
    mxDistanceFromTheSun = 1
    mxType = 1
    mxID = 1
    for i in dict:
        mxId = max(len(i), mxId)
        mxName = max(len(str(dict[i][0])), mxName)
        mxRadius = max(len(str(dict[i][1])), mxRadius)
        mxWeight = max(len(str(dict[i][2])), mxWeight)
        mxDistanceFromTheSun = max(len(str(dict[i][3])), mxDistanceFromTheSun)
        mxType = max(len(str(dict[i][4])), mxType)
        mxID = max(len(str(dict[i][5])), mxID)
    return mxId, mxName, mxRadius, mxWeight, mxDistanceFromTheSun, mxType, mxID
 
def printerDB():
    db = read()
    mxId, mxName, mxRadius, mxWeight, mxDistanceFromTheSun, mxType, mxID = maxLen(db)
    s0Id = "N" + " " * (mxId - len("id")) + " |"
    mxId = len(s0Id)-2
    s0Name = "Название" + " " * (mxName - len("Название")) + " |"
    mxName = len(s0Name)-2
    s0Radius = "Радиус" + " " * (mxRadius - len("Радиус")) + " |"
    mxRadius = len(s0Radius)-2
    s0Weight = "Весс" + " " * (mxWeight - len("Весс")) + " |"
    mxWeight = len(s0Weight)-2
    s0DistanceFromTheSun = "Растояние до солнца" + " " * (mxDistanceFromTheSun - len("Растояние до солнца")) + " |"
    mxDistanceFromTheSun = len(s0DistanceFromTheSun)-2
    s0Type = "Тип" + " " * (mxType - len("Тип")) + " |"
    mxType = len(s0Type)-2
    s0mxID = "ID" + " " * (mxID - len("ID")) + " |"
    mxID = len(s0mxID)-2
    print(s0Id, s0Name, s0Radius, s0Weight, s0DistanceFromTheSun, s0Type, s0mxID)
    for i in db:
        siId = str(i) + " " * (mxId - len(str(i))) + " |"
        siName = str(db[i][0]) + " " * (mxName - len(str(db[i][0]))) + " |"
        siRadius = str(db[i][1]) + " " * (mxRadius - len(str(db[i][1]))) + " |"
        siWeight = str(db[i][2]) + " " * (mxWeight - len(str(db[i][2]))) + " |"
        siDistanceFromTheSun = str(db[i][3]) + " " * (mxDistanceFromTheSun - len(str(db[i][3]))) + " |"
        siType = str(db[i][4]) + " " * (mxType - len(str(db[i][4]))) + " |"
        siID = str(db[i][5]) + " " * (mxID - len(str(db[i][5]))) + " |"
        print(siId, siName, siRadius, siWeight, siDistanceFromTheSun, siType, siID)
    
def sortListPlanet(list, pole):
    planet.whatsr = pole
    list = list 
    for i in range(0, len(list)):
        ind = i
        for j in range(i+1, len(list)):
            if list[j] <= list[ind]:
                ind = j
        list[i], list[ind] = list[ind], list[i]
    return list


# если БД это лист
# 1) ??? мб read()
# 2) list.append(your element)
# 3) sortListPlanet - Сортировка БД по выбранному полю
# 4) тоже что и 2
# 5) list.pop(id element in list(array))
# 6) list[id element in list(array)] = new planet element
# 6) list[id element in list(array)][id field in the element] = new value
# 7) printerlistr

def printerlistr():
    for i in arrayPlanet:
        print(i)


# 3
mars = planet("марс", 1000, 2000000, 40000000, "roc")
upitr = planet("юпитер", 1, 1, 300, "gas")
vinera = planet("винера", 200, 30, 45, "roc")
mars2 = planet("марс2", 1000, 2000000, 40, "roc")
arrayPlanet = [mars, upitr, vinera, mars2]
for i in arrayPlanet:
    print(i)
    addElenment(i)

for i in arrayPlanet:
    print(i.name, i.radius)
print()
sortListPlanet(arrayPlanet, "radius")
for i in arrayPlanet:
    print(i.name, i.radius)

# write({})
# print(mars)

# print(read())
# addElenment(vinera)
# addElenment(mars)
# addElenment(vinera)
# addElenment(mars2)
# addElenment(vinera)
# addElenment(mars2)
# addElenment(vinera)
# addElenment(mars)
# addElenment(vinera)
# addElenment(mars)
# print(read())
# sortDB("radius")
# # chengeElement(0, ['винера', 200, 30, 45, 'roc'])
# print(read())
# printerDB()
