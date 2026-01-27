import random


def sortVyborom(array):
    colPerestan = 0
    colsravn = 0
    for i in range(len(array)):
        # array[i], array[indexMinElrmrnt] = array[indexMinElrmrnt], array[i] = array.index(min(array[i:]))
        # print(array[i], i, array[indexMinElrmrnt], indexMinElrmrnt)
        # array[i], array[indexMinElrmrnt] = array[indexMinElrmrnt], array[i]
        indexMinElrmrnt = i
        for j in range(i, len(array)):
            colsravn += 1
            if array[indexMinElrmrnt] > array[j]:
                indexMinElrmrnt = j
        colPerestan += 1
        array[i], array[indexMinElrmrnt] = array[indexMinElrmrnt], array[i]
    return array, colPerestan, colsravn

def sortPuzir(array):
    colPerestan = 0
    colsravn = 0
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            colsravn += 1
            if array[j - 1] > array[j]:
                colPerestan += 1
                array[j - 1], array[j] = array[j], array[j - 1]
    return array, colPerestan, colsravn

def sortSliyaniem(array):
    print("fff")
    colPerestan = 0
    colsravn = 0
    array1 = array[:len(array) // 2]
    array2 = array[len(array) // 2:]
    print(array1)
    print(array2)
    rezForArray1 = sortPuzir(array1)
    rezForArray2 = sortPuzir(array2)
    print(rezForArray1)
    print(rezForArray2)
    sortedArray1 = rezForArray1[0]
    sortedArray2 = rezForArray2[0]
    colPerestan += rezForArray1[1] + rezForArray2[1]
    colsravn += rezForArray1[2] + rezForArray2[2]

    rezArray = ["*"] * len(array)
    i = 0
    j = 0
    while i < len(sortedArray1) and j < len(sortedArray2):
        colsravn += 1
        if sortedArray1[i] <= sortedArray2[j]:
            rezArray[i + j] = sortedArray1[i]
            i += 1
        else:
            rezArray[i + j] = sortedArray2[j]
            j += 1
    while i < len(sortedArray1):
        rezArray[i + j] = sortedArray1[i]
        i += 1
    while j < len(sortedArray2):
        rezArray[i + j] = sortedArray2[j]
        j += 1
    return rezArray, colPerestan, colsravn

"""3 5 2 7 1 67 23 45 3 """

def vivod(maxColElementRow, array, colPerestan, colsravn):
    lenMinElement = len(str(min(array)))
    lenMaxElement = len(str(max(array)))
    lenH = max(lenMinElement, lenMaxElement) + 2
    if maxColElementRow == None:
        maxColElementRow = 5
    colPrintElemrnt = 0
    for i in range((len(array) // maxColElementRow) + 1):
        if colPrintElemrnt == len(array):
            print(f"\nколичество перестановок: {colPerestan} \nколичество сравнений: {colsravn}")
            return True
        for j in range(maxColElementRow):
            if colPrintElemrnt == len(array):
                print(f"\nколичество перестановок: {colPerestan} \nколичество сравнений: {colsravn}")
                return True
            print(str(array[maxColElementRow * i + j]).rjust(lenH), end="")
            colPrintElemrnt += 1
        print()

def rendomArray(cloNumberInDemonstration):
    demoArray = [0] * cloNumberInDemonstration
    for i in range(cloNumberInDemonstration):
        demoArray[i] = random.randint(0, 99)
    return demoArray

def demonstration(cloNumberInDemonstration):
    demoArray = rendomArray(cloNumberInDemonstration)
    print("изначальный массива")
    vivod(6, demoArray, 0 ,0 )
    rezSortPuz = sortPuzir(demoArray)
    print("вот массив  отсортированный пузырьком")
    vivod(6, rezSortPuz[0], rezSortPuz[1], rezSortPuz[2])
    rezSortVibor = sortVyborom(demoArray)
    print("вот массив  отсортированный выбором")
    vivod(6, rezSortVibor[0], rezSortVibor[1], rezSortVibor[2])
    rezSortSliyaniem = sortSliyaniem(demoArray)
    print("вот массив отсортированный 'Сортировка слиянием'")
    vivod(6, rezSortSliyaniem[0], rezSortSliyaniem[1], rezSortSliyaniem[2])
    main()

def MbChengArray():
    print("нажмите C для изменения размера массива(по умолчанию 20), A для ввода своего массива или P для пропуска")
    userInput = input()
    if userInput == "C":
        print("введите длину(натуральное число) списка")
        try:
            newLan = int(input())
            return newLan, True, 1
        except:
            return None, False
    elif userInput == "A":
        print("введите последовательность чисел в одну строку разделяя их пробелами")
        try:
            newArray = list(map(int, input().split()))
            return newArray, True, 2
        except:
            return None, False
    elif userInput == "P":
            return None, True
    else:
        return None, False

def otherSort(array, LenArray):
    print("введите A для сортировки пузырьком, B дял сортировки выбором и C для сортировки слиянием")
    userInputSort = input()
    if userInputSort == "A":
        return sortPuzir(array)
    elif userInputSort == "B":
        return sortVyborom(array)
    elif userInputSort == "C":
        return sortSliyaniem(array)
    else:
        print("некорректный ввод")
        workWithUserArray(array, LenArray)

def workWithUserArray(array, LenArray, arrayForWork):
    if array == None:
        if LenArray == None:
            array = rendomArray(20)
            arrayForWork = [array, 0, 0]
        else:
            array = rendomArray(LenArray)
            arrayForWork = [array, 0, 0]
    if arrayForWork == None:
        arrayForWork = [array, 0, 0]
    if LenArray == None:
        LenArray = len(array)
    print("введите A для вывода массива, B для сортировки и любой другой символ для перехода в главное меню")
    userAction = input()
    print(array)
    print(LenArray)
    print(arrayForWork)
    if userAction == "A":
        vivod(None, arrayForWork[0], arrayForWork[1], arrayForWork[2])
    elif userAction == "B":
        rez = otherSort(array[:], LenArray)
        arrayForWork = [rez[0], rez[1], rez[2]]
    else:
        main()

    workWithUserArray(array, LenArray, arrayForWork)


def wokWithUserInput():
    print("нажмите C для изменения массива или P для пропуска")
    userInput = input()
    if userInput == "C":
        rez = MbChengArray()
        if rez[1]:
            if rez[2] == 1:
                workWithUserArray(None, rez[0], None)
            elif rez[2] == 2:
                workWithUserArray(rez[0], len(rez[0]), None)
        else:
            print("что-то пошло не так")
            main()
    elif userInput == "P":
        workWithUserArray(None, None, None)
    else:
        print("некорректный ввод")
        main()


def main():
    print("привет введи D для того чтобы я показал как работает программа\n"
          "и I для другой работы с программой")
    userInput = input()
    if userInput == "D":
        demonstration(20)
    elif userInput == "I":
        wokWithUserInput()
    else:
        print("некоректный ввод")
        main()

if main() == "__name__":
    main()
