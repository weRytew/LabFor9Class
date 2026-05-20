import json
from plenet import planet
# from resept import resept

class DB:
    cl = None

    def __init__(self, name, settingsPrint, cl):
        self.__name = name
        self.loc = []
        self.settingsPrint = settingsPrint
        DB.cl = cl
        try:
            with open(f"{name}.json", "r", encoding="utf-8") as file:
                a = 1
        except:
            with open(f"{name}.json", "w", encoding="utf-8") as file:
                print("{}", file=file)
    
    def read(self):
        with open(f"{self.__name}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    
    def jsonToList(self, js: dict):
        ls = [0]*len(js)
        counter = 0
        for i in js:
            ls[counter] = DB.cl.create(js[i][:-1])
            counter += 1
        return ls

    def write(self, data: dict):
        if type(data) == dict:
            with open(f"{self.__name}.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            print("не словать")
    
    def sortt(self, what):
        DB.cl.whatsr = what
        array = self.loc
        for i in range(0, len(array)):
            ind = i
            for j in range(i+1, len(array)):
                if array[j] <= array[ind]:
                    ind = j
            array[i], array[ind] = array[ind], array[i]
        self.loc = array
    
    def add(self, newEl):
        self.loc.append(newEl)
    
    def dell(self, idInLoc):
        self.loc.pop(idInLoc)
    
    def chenge(self, newel, idInLoc):
        self.loc[idInLoc] = newel
    
    def fnd(self, name):
        for i in self.loc:
            if i.__name == name:
                return i
        return "not faund"
    
    def maxLen(self, dict):
        mxId = 1
        mxName = 1
        mxRadius = 1
        mxWeight = 1
        mxDistanceFromTheSun = 1
        mxType = 1
        mxID = 1
        for i in dict:
            mxId = max(len(str(i)), mxId)
            mxName = max(len(str(dict[i][0])), mxName)
            mxRadius = max(len(str(dict[i][1])), mxRadius)
            mxWeight = max(len(str(dict[i][2])), mxWeight)
            mxDistanceFromTheSun = max(len(str(dict[i][3])), mxDistanceFromTheSun)
            mxType = max(len(str(dict[i][4])), mxType)
            mxID = max(len(str(dict[i][5])), mxID)
        return mxId, mxName, mxRadius, mxWeight, mxDistanceFromTheSun, mxType, mxID
    
    def printerDB(self):
        db = self.listToDict()
        mxId, mxName, mxRadius, mxWeight, mxDistanceFromTheSun, mxType, mxID = self.maxLen(db)
        s0Id = "N" + " " * (mxId - len("id")) + " |"
        mxId = len(s0Id)-2
        s0Name = f"{self.settingsPrint[0]}" + " " * (mxName - len(f"{self.settingsPrint[0]}")) + " |"
        mxName = len(s0Name)-2
        s0Radius = f"{self.settingsPrint[1]}" + " " * (mxRadius - len(f"{self.settingsPrint[1]}")) + " |"
        mxRadius = len(s0Radius)-2
        s0Weight = f"{self.settingsPrint[2]}" + " " * (mxWeight - len(f"{self.settingsPrint[2]}")) + " |"
        mxWeight = len(s0Weight)-2
        s0DistanceFromTheSun = f"{self.settingsPrint[3]}" + " " * (mxDistanceFromTheSun - len(f"{self.settingsPrint[3]}")) + " |"
        mxDistanceFromTheSun = len(s0DistanceFromTheSun)-2
        s0Type = f"{self.settingsPrint[4]}" + " " * (mxType - len(f"{self.settingsPrint[4]}")) + " |"
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
    
    def listToDict(self):
        dict = {}
        for i in range(len(self.loc)):
            dict[i] = self.loc[i].getDataList()
        return dict