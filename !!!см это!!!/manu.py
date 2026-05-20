from dbggg import DB

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

def manu(nameDB, cl, sbAdd, sbSort, stP):
    print("m для доступных команд")
    db = DB(nameDB, stP, cl)
    work = True
    while work:
        er = False
        userInput = input().strip()
        # try:
        if userInput == "m":
            printAllcomands()
        elif userInput == "load db":
            dbjs = db.read()
            db.loc = db.jsonToList(dbjs)
        elif userInput == "save db":
            dbjs = db.listToDict()
            db.write(dbjs)
        elif userInput == "print":
            db.printerDB()
        elif userInput == "append in":
            # "имя;категория;время приготовления;ингридиенты(a b c итд);сложность"
            print(sbAdd)
            newEl = cl.create(input().split(";"))
            db.add(newEl)
        elif userInput == "find":
            print("название")
            usInp2 = input().strip()
            print(db.fnd(usInp2))
        elif userInput == "chenge":
            # "номер в списке;(далие измененный обьект)имя;категория;время приготовления;ингридиенты(a b c итд);сложность"
            print("номер в списке;" + sbAdd)
            usInp2 = input().split(";")
            db.chenge(cl.create(usInp2[1:]), int(usInp2[0]))
        elif userInput == "del":
            print("номер в списке")
            usInp2 = int(input())
            db.dell(usInp2)
        elif userInput == "sort":
            # "по чему: name\n categoray\n timeForCook\n ingredients\n level"
            print(sbSort)
            usInp2 = input().strip()
            db.sortt(usInp2)
        elif userInput == "exit":
            work = False
        else:
            er = True
        if not er:
            print("successfully")
        else:
            print("error")
        # except:
        #     print("error")