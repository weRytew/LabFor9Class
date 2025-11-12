def Hour(hourArray, userInputHour):
    if userInputHour > 12:
        userInputHour -= 12

    resaltStrForHour = f"{userInputHour}"

    if userInputHour == 0 or 5 <= userInputHour <= 12:
        resaltStrForHour += hourArray[0]
    elif userInputHour == 1:
        resaltStrForHour += hourArray[1]
    else:
        resaltStrForHour += hourArray[2]
    return resaltStrForHour

def Minut(minutArray, userInputMinut):
    resaltStrForMinut = ""

    if userInputMinut == 0:
        resaltStrForMinut = "ровно"
        return resaltStrForMinut
    else:
        resaltStrForMinut = f"{userInputMinut}"

    tenMinut = userInputMinut // 10
    minut = userInputMinut % 10

    if minut == 1 and tenMinut != 1:
        resaltStrForMinut += minutArray[0]
    elif str(minut) in "3 2 4" and tenMinut != 1:
        resaltStrForMinut += minutArray[1]
    else:
        resaltStrForMinut += minutArray[2]

    return  resaltStrForMinut

def TimesofDay(userInputHour, userInputMinut, timesofDay):
    if userInputHour == 12 and userInputMinut == 00:
        return timesofDay[5]
    elif userInputHour == 0 and userInputMinut == 00:
        return timesofDay[4]
    return timesofDay [userInputHour // 6]

def processingTime(userInput):
    hourArray = [" часов", " час", " часа"]
    minutArray = [" минута", " минуты", " минут"]
    timesofDay = ["ночи", "утра", "дня", "вечера", "полночь", "полдень"]

    hour = Hour(hourArray, userInput[0])
    minut = Minut(minutArray, userInput[1])
    time = TimesofDay(userInput[0], userInput[1], timesofDay)
    if time == timesofDay[4] or time == timesofDay[5]:
        print(time)
    elif minut == "ровно":
        print(hour + " " + time + " " + minut)
    else:
        print(hour + " " + minut + " " + time)

def Main():
    print("введите время с 00:00 до 23:59 в формате часы пробелы минуты(часы и минуты должны быть целыми числами/цифрами)")
    userInput = input().split()
    lenUserInput = True
    if len(userInput) != 2:
    	lenUserInput = False
    	
    hour = userInput[0]
    hourChek = False
    minut = userInput[1]
    minutChek = False
    for i in range(0, 24):
    	if hour == str(i) or hour == "0"+str(i):
    		hourChek = True
    for i in range(0, 60):
    	if minut == str(i) or minut == "0"+str(i):
    		minutChek = True
    if not lenUserInput:
    	print("тутуту...")
    if hourChek and minutChek and lenUserInput:
        userInput2 = list(map(int, userInput))
        #userInput2 = [int(hour), int(minut)]
        processingTime(userInput2)
    if not hourChek:
        print("Введены недопустимые данные: часы должны быть от 0 до 23")
    if not minutChek:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59")

if __name__ == "__main__":
    Main()
