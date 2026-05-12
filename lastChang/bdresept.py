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

def jsonToList(js: dict):
    ls = [0]*len(js)
    counter = 0
    for i in js:
        ls[counter] = resept.create(js[i][:-1])[0]
        counter += 1
    return ls
# 2
def write(data):
    if type(data) == list:
        data = listToJs(data)
    with open("db.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def listToJs(ls: list[resept]):
    js = {}
    for i in range(len(ls)):
        js[i] = ls[i].getDataList()
    return js

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
    s0Radius = "Категория" + " " * (mxRadius - len("Категория")) + " |"
    mxRadius = len(s0Radius)-2
    s0Weight = "время готовки" + " " * (mxWeight - len("время готовки")) + " |"
    mxWeight = len(s0Weight)-2
    s0DistanceFromTheSun = "ингридиенты" + " " * (mxDistanceFromTheSun - len("ингридиенты")) + " |"
    mxDistanceFromTheSun = len(s0DistanceFromTheSun)-2
    s0Type = "сложность" + " " * (mxType - len("сложность")) + " |"
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
def fnd(name, wher, ls: list[resept]):
    if wher == "db":
        d = read()
        for i in d:
            if d[i][0] == name: return resept.create(d[i][:-1])[0]
    elif wher == "ls":
        for i in ls:
            if i.name == name:
                return i
    return "not faund"

# 6
def chengeElement(index, newElement):
    try:
        print("ggggggggggggggggggggggggggggggggggggggggggggggg")
        newElement = newElement[0]
        if type(newElement) == resept:
            dict = read()
            print(dict)
            dict[index] = newElement.getDataList()
            write(dict)
            return True
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

def printAllcomands():
    print("доступные команды:")
    print(" load db")
    print(" save db")
    print(" print")
    print(" append in")
    print(" find")
    print(" chenge")
    print(" del")
    print(" sort")
    print(" exit")
# 9 CSV

def main():
    db: list[resept] = []
    work = True
    print("m для доступных команд")
    while work:
        er = False
        userInput = input().strip()
        try:
            if userInput == "m":
                printAllcomands()
            elif userInput == "load db":
                dbjs = read()
                db = jsonToList(dbjs)
            elif userInput == "save db":
                write(db)
            elif userInput == "print":
                print("db or list?")
                usInp = input()
                if usInp == "db":
                    printerDB()
                elif usInp == "list":
                    p(db)
            elif userInput == "append in":
                print("db or list?")
                usInp = input().strip()
                print("имя;категория;время приготовления;ингридиенты(a b c итд);сложность")
                newEl =  resept.create(input().split(";"))
                if usInp == "db":
                    if newEl[1] != False:
                        addElenment(newEl[0])
                    else:
                        er = True
                elif usInp == "list":
                    if newEl[1] != False:
                        db.append(newEl[0])
                    else:
                        er = True
            elif userInput == "find": # дописать
                print("db or list?")
                usInp = input().strip()
                if usInp == "db":
                    print("название")
                    usInp2 = input().strip()
                    print(fnd(usInp2, "db", []))
                elif usInp == "list":
                    print("название")
                    usInp2 = input().strip()
                    print(fnd(usInp2, "ls", db))
            elif userInput == "chenge":
                print("db or list?")
                usInp = input().strip()
                if usInp == "db":
                    print("номер в бд;(далие измененный обьект)имя;категория;время приготовления;ингридиенты(a b c итд);сложность")
                    usInp2 = input().split(";")
                    lk = chengeElement(usInp2[0], resept.create(usInp2[1:]))
                    if lk == None:
                        er = True
                elif usInp == "list":
                    print("номер в списке;(далие измененный обьект)имя;категория;время приготовления;ингридиенты(a b c итд);сложность")
                    usInp2 = input().split(";")
                    db[int(usInp2[0])] = resept.create(usInp2[1:])
            elif userInput == "del":
                print("db or list?")
                usInp = input().strip()
                if usInp == "db":
                    print("номер в бд")
                    usInp2 = int(input())
                    delElement(usInp2)
                elif usInp == "list":
                    print("номер в списке")
                    usInp2 = int(input())
                    db.pop(usInp2)
            elif userInput == "sort":
                print("db or list?")
                usInp = input().strip()
                if usInp == "db":
                    print("по чему: name\n categoray\n timeForCook\n ingredients\n level")
                    usInp2 = input().strip()
                    sortDB(usInp2)
                elif usInp == "list":
                    usInp2 = input().strip()
                    print("по чему: name\n categoray\n timeForCook\n ingredients\n level")
                    sortListPlanet(db, usInp2)
            elif userInput == "CSV": # дописать
                print()
            elif userInput == "exit":
                work = False
            else:
                er = True
            if not er:
                print("successfully")
            else:
                print("error")
        except:
            print("error")

if __name__ == "__main__":
    main()
