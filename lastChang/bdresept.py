import json
from resept import resept

# 1
def read():
    try:
        with open("db.json", "r", encoding="utf-8") as file:
            a = 1
    except:
        with open("db.json", "w", encoding="utf-8") as file:
            print("{}", file=file)
    with open("db.json", "r", encoding="utf-8") as file:
        return json.load(file)

# 2
def write(data):
    with open("db.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 3
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

def p(db: list):
    counter = 0
    for i in db:
        print(counter, i)
        counter += 1

# 4
def addElenment(newData: resept):
    lastData = read()
    updatingData = lastData
    updatingData[len(lastData)] = newData.getDataList()
    write(updatingData)

# 5 - finder

# 6
def chengeElement(index, newElement):
    try:
        if len(newElement) == 5 and type(newElement) == list:
            dict = read()
            dict[index] = resept.getDataList(newElement)
            write(dict)
        else:
            return None
    except:
        print("Ошибка при изменении")
        return None

# 7
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

# 8
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
    if resept.whatsr == "name":
        return dataElement[0]
    if resept.whatsr == "categoray":
        return dataElement[1]
    if resept.whatsr == "timeForCook":
        return dataElement[2]
    if resept.whatsr == "ingredients":
        return dataElement[3]
    if resept.whatsr == "level":
        return dataElement[4]

def sortDB(pole):
    resept.whatsr = pole
    planetDiction = read()
    planetList = dictToList(planetDiction)
    planetList.sort(key=howSortFunc)
    dict = listToDict(planetList)
    write(dict)

def sortListPlanet(list, pole):
    resept.whatsr = pole
    list = list 
    for i in range(0, len(list)):
        ind = i
        for j in range(i+1, len(list)):
            if list[j] <= list[ind]:
                ind = j
        list[i], list[ind] = list[ind], list[i]
    return list

# 9 CSV

def main():
    db = []
    work = True
    while work:
        userInput = input()
        if userInput == "load db":
            db = read()
        elif userInput == "save":
            write(db)
        elif userInput == "print db":
            usInp = input()
            if usInp == "db":
                printerDB()
            elif usInp == "list":
                p(db)
        elif userInput == "append":
            usInp = input()
            if usInp == "db":
                newEl =  resept.create(input().split(";"))
                if newEl[1] != False:
                    addElenment(newEl[0])
                    print("good")
                else:
                    print("bed")
            elif usInp == "list":
                newEl =  resept.create(input().split(";"))
                if newEl[1] != False:
                    db.append(newEl[0])
                    print("good")
                else:
                    print("bed")
        elif userInput == "find": # дописать
            print()
        elif userInput == "chenge":
            usInp = input()
            if usInp == "db":
                usInp2 = input().split(";")
                chengeElement(int(usInp2[0]), resept.create(usInp2))
            elif usInp == "list":
                usInp2 = input().split(";")
                db[int(usInp2[0])] = resept.create(usInp2)
        elif userInput == "del":
            usInp = input()
            if usInp == "db":
                usInp2 = int(input())
                delElement(usInp2)
            elif usInp == "list":
                usInp2 = int(input())
                db.pop(usInp2)
        elif userInput == "sort":
            usInp = input()
            if usInp == "db":
                usInp2 = input()
                sortDB(usInp2)
            elif usInp == "list":
                usInp2 = int(input())
                sortListPlanet(db, usInp2)
        elif userInput == "CSV": # дописать
            print()
        elif userInput == "exit":
            work = False
        print("next")

if __name__ == "__main__":
    main()