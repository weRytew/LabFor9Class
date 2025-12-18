"""
    получаем ввод пользователя
        получаем ввод
        проверяем его на корректность
            в воде всего 2 числа
            первое число находиться в диапазоне от [0;23]
            второе число находиться в диапазоне от [0;59]
        если все ок
            работаем с часами
                если введенный час больше 12 заменяем его на час - 12
                определяем окончание(их всего 3) часа(возможно измененного) и возвращаем ответ(слово с нужным окончанием)
            работаем с минутами
                проверяем на исключения(xx 00)
                если минута - исключение
                    возвращаем ответ(ровно)
                иначе
                    определяем окончание(их всего 3) и возвращаем ответ(слово с нужным окончанием)
            работаем с временем суток
                определяем ночь, утро, день, полдень или полночь соответствует введенному часу и возвращаем нужное
            вывод результата
                если время - полдень или полночь
                    выводим полдень или полночь
                если ровно то
                    выводим часы + ровно
                иначе
                    выводим часы + минуты
        иначе
            выводим надпись о некорректности ввода
"""

"""
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
    checkLenUserInput = True
    checkInputHour = False
    checkInputMinut = False
    if len(userInput) != 2:
        checkLenUserInput = False
    else:
        hour = userInput[0]
        minut = userInput[1]
        for i in range(0, 24):
            if hour == str(i) or hour == "0"+str(i):
                checkInputHour = True
        for i in range(0, 60):
            if minut == str(i) or minut == "0"+str(i):
                checkInputMinut = True
    if not checkLenUserInput:
        print("тутуту...")
    if checkInputHour and checkInputMinut and checkLenUserInput:
        userInput2 = list(map(int, userInput))
        processingTime(userInput2)
    if not checkInputHour:
        print("Введены недопустимые данные: часы должны быть от 0 до 23")
    if not checkInputMinut:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59")

if __name__ == "__main__":
    Main()
"""


"""
    получем данные
    проверяем их на коректность
    если ок
        выбираем нужное скланение слова час
            1) переводим полученные часы в нужную форму(на пример если 
               получили 16 переводим в 4. те если полученый час больше 12 
               отнимаем от него 12)
            2) выбираем нужное скланение слова час(есди введенный час 0, 5-12
               то выбираем "часов", если 1 то час, а если 2-4 то часа )
        выбираем нужное скланение слова минута
            если введенные минуты равны 0 то выбираем ровно
            иначе 
                считам количество десятков и количество единиц в 
                веденных минутах
                если в единици менут равны 1 и введенные минуты это не 10-19
                то выбираем минута
                если в единици менут равны 2, 3 или 4 и введенные минуты 
                это не 10-19 то выбираем минуты
                иначе выбираем минут
        выбираем нужное время суток
            если введенные минуты равны 0 и введенные часы равны 12 
            то выцбираем полдень
            если введенные минуты равны 0 и введенные часы равны 0
            то выцбираем полночь
            иначе выбираем ночи если ввыденные часы с 0-5,
            утра если ввыденные часы с 6-11,
            дня если ввыденные часы с 12-17 и 
            вечера если ввыденные часы с 18-23 
        выводим результат
"""



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
    if len(userInput) == 1:
        userInput.append("0")
    checkLenUserInput = True
    checkInputHour = False
    checkInputMinut = False
    if len(userInput) != 2:
        checkLenUserInput = False
    else:
        hour = userInput[0]
        minut = userInput[1]
        for i in range(0, 24):
            if hour == str(i) or hour == "0"+str(i):
                checkInputHour = True
        for i in range(0, 60):
            if minut == str(i) or minut == "0"+str(i):
                checkInputMinut = True
    if not checkLenUserInput:
        print("тутуту...")
    if checkInputHour and checkInputMinut and checkLenUserInput:
        userInput2 = list(map(int, userInput))
        processingTime(userInput2)
    if not checkInputHour:
        print("Введены недопустимые данные: часы должны быть от 0 до 23")
    if not checkInputMinut:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59")

if __name__ == "__main__":
    Main()
