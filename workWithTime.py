def Hour(hourArray, userInputHour):
    if userInputHour > 12:
        userInputHour -= 12
    resaltStrForHour = f"{userInputHour}"
    #resaltStrForHour += namberValuesArrayForHour[userInputHour]
    if userInputHour == 0 or 5 <= userInput[0] <= 12:
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
    elif str(minut) in "1 2" and tenMinut != 1:
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

def Main(userInput):
    hourArray = [" часов", " час", " часа"]
    minutArray = [" минута", " минуты", " минут"]
    timesofDay = ["ночи", "утора", "дня", "вечера", "полночь", "полдень"]

    hour = Hour(hourArray, userInput[0])
    minut = Minut(minutArray, userInput[1])
    time = TimesofDay(userInput[0], userInput[1], timesofDay)
    if time == timesofDay[4] or time == timesofDay[5]:
        print(time)
    elif minut == "ровно":
        print(hour + " " + time + " " + minut)
    else:
        print(hour + " " + minut + " " + time)

print("введите время с 00:00 до 23:59 в формате часы пробелы минуты(часы и минуты должны быть целыми числами/цифрами)")
userInput = list(map(int, input().split()))

if 0 <= userInput[0] <= 23 and 0 <= userInput[1] <= 59:
    Main(userInput)
if 0 > userInput[0] or userInput[0] > 23:
    print("Введены недопустимые данные: часы должны быть от 0 до 23")
if 0 > userInput[1] or userInput[1] > 59:
    print("Введены недопустимые данные: минуты должны быть от 0 до 59")
