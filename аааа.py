def Hour(namberValuesArrayForHour, hourArray, userInputHour):
    if userInputHour > 12:
        userInputHour -= 12
    resaltStrForHour = ""
    resaltStrForHour += namberValuesArrayForHour[userInputHour]
    if userInputHour == 0 or 5 <= userInput[0] <= 12:
        resaltStrForHour += hourArray[0]
    elif userInputHour == 1:
        resaltStrForHour += hourArray[1]
    else:
        resaltStrForHour += hourArray[2]
    return resaltStrForHour

def Minut(namberValuesArrayForMinut, namberValuesArrayForMinutTen, minutArray, userInputMinut):
    resaltStrForMinut = ""
    tenMinut = userInputMinut // 10
    minut = userInputMinut % 10
    if userInputMinut <= 12:
        resaltStrForMinut += namberValuesArrayForMinut[userInputMinut]
        if userInputMinut == 0:
            return resaltStrForMinut
    elif 13 <= userInputMinut <= 19:
        resaltStrForMinut += namberValuesArrayForMinut[(userInputMinut % 10)] + "ндцать"
    else:
        resaltStrForMinut += namberValuesArrayForMinutTen[tenMinut] + " " + namberValuesArrayForMinut[minut]

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



print("введите время с 00:00 до 23:59 в формате часы пробелы минуты(часы и минутыв должны быть целыми числами/цифрами)")
userInput = list(map(int, input().split()))

if 0 <= userInput[0] <= 23 and 0 <= userInput[1] <= 59:

    namberValuesArrayForHour = ["ноль", "один", "два", "три", "читыре", "пять", "шесть", "семь", "восемь", "девять",
                                "десять", "одинадцать", "двенадцать"]
    hourArray = [" часов", " час", " часа"]

    namberValuesArrayForMinut = ["ровно", "одна", "две", "три", "читыре", "пять", "шесть", "семь", "восемь", "девять",
                                 "десять", "одинадцать", "двенадцать"]
    namberValuesArrayForMinutTen = ["", "", "двaдцать", "тридцать", "сорак", "пятдесят"]
    minutArray = [" минута", " минуты", " минут"]
    timesofDay = ["ночи", "утора", "дня", "вечера", "полночь", "полдень"]

    hour = Hour(namberValuesArrayForHour, hourArray, userInput[0])
    minut = Minut(namberValuesArrayForMinut, namberValuesArrayForMinutTen, minutArray, userInput[1])
    time = TimesofDay(userInput[0], userInput[1], timesofDay)
    if time == timesofDay[4] or time == timesofDay[5]:
        print(time)
    elif minut == namberValuesArrayForMinut[0]:
        print(hour + " " + time + " " + minut)
    else:
        print(hour + " " + minut + " " + time)
else:
    print("долбоеб прочитай что тебя просили ввести и попробуй снова")
