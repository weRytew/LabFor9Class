import random

def sortVyborom(array):
    colPerestan = 0
    colsravn= 0
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
        for j in range(1, len(array)-i):
            colsravn += 1
            if array[j-1] > array[j]:
                colPerestan += 1
                array[j-1], array[j] = array[j], array[j-1]
    return array, colPerestan, colsravn

def sortSliyaniem(array):
    colPerestan = 0
    colsravn = 0
    array1 = array[:len(array)//2]
    array2 = array[len(array)//2:]
    rezForArray1 = sortPuzir(array1)
    rezForArray2 = sortPuzir(array2)
    sortedArray1 = rezForArray1[0]
    sortedArray2 = rezForArray2[0]
    colPerestan += rezForArray1[1] + rezForArray2[1]
    colsravn += rezForArray1[2] + rezForArray2[2]

    if len(array) % 2 != 0:
        array1.append("x")
    k = ["*"]*len(array)
    i = 0
    j = 0
    jgran = False
    igran = False
    while i + j < len(array):
        colsravn += 1
        if jgran:
            colsravn += 1
            k[i + j] = sortedArray1[i]
            i += 1
        elif igran:
            colsravn += 1
            k[i + j] = sortedArray2[j]
            j += 1
        elif sortedArray1[i] != "x" and sortedArray1[i] <= sortedArray2[j]:
            colsravn += 1
            k[i + j] = sortedArray1[i]
            i += 1
            if i == len(sortedArray1):
                igran = True
        elif sortedArray1[i] != "x" and sortedArray1[i] >= sortedArray2[j]:
            colsravn += 1
            k[i + j] = sortedArray2[j]
            j += 1
            if j == len(sortedArray2):
                jgran = True
    return k, colPerestan, colsravn

def vivod(maxColElementRow, array, colPerestan, colsravn):
    lenMinElement = len(str(min(array)))
    lenMaxElement = len(str(max(array)))
    lenH = max(lenMinElement, lenMaxElement) + 2
    if maxColElementRow == None:
        maxColElementRow = 10
    colPrintElemrnt = 0
    for i in range((len(array)//maxColElementRow) + 1):
        if colPrintElemrnt == len(array):
            print(f"количество перестановок: {colPerestan} \nколичество сравнений: {colsravn}")
            return True
        for j in range(maxColElementRow):
            if colPrintElemrnt == len(array):
                print(f"количество перестановок: {colPerestan} \nколичество сравнений: {colsravn}")
                return True
            print(str(array[maxColElementRow*i+j]).rjust(lenH), end="")
            colPrintElemrnt += 1
        print()

def demonstration(cloNumberInDemonstration):
    demoArray = [0]*cloNumberInDemonstration
    for i in range(cloNumberInDemonstration):
        demoArray[i] = random.randint(0, 99)
    rezSortPuz = sortPuzir(demoArray)
    print("вот масив  отсортированный пузырьком")
    vivod(6, rezSortPuz[0], rezSortPuz[1], rezSortPuz[2])
    rezSortVibor = sortVyborom(demoArray)
    print("вот масив  отсортированный выбором")
    vivod(6, rezSortVibor[0], rezSortVibor[1], rezSortVibor[2])
    rezSortSliyaniem = sortSliyaniem(demoArray)
    print("вот масив отсортированный 'Сортировка слиянием'")
    vivod(6, rezSortSliyaniem[0], rezSortSliyaniem[1], rezSortSliyaniem[2])

def MbChengArray():
    print("нажмите C для изменения размера массива(по умолчанию 20), A для ввода своего массива или P для пропуска")
    userInput = input()
    if userInput == "C":
        print("введите длину(натуральное число) списка")
        try:
            newLan = int(input())
            return newLan, True, 1
        except:
            print("что-то пошло нетак")
            return None, False, 0
    if userInput == "A":
        print("введите последовательность чисел в одну строку раздиляя их пробелами")
        try:
            newArray = list(map(int, input().split()))
            return newLan, True, 2
        except:
            print("что-то пошло нетак")
            return None, False, 0
    else:
        print("некоректный ввод")
        return None, False, 0

def workWithUserArray(array, LenArray):


def wokWithUserInput():
    print("нажмите C для изменения массива или P для пропуска")
    userInput = input()
    if userInput == "C":
        rez = MbChengArray()
        if rez[1]:
            if rez[2] == 1:
                workWithUserArray(None, rez)
            if rez[2] == 2:
                workWithUserArray(rez[0])
    if userInput == "P":
        workWithUserArray(rez[0])
    else:
        print("некоректный ввод")
        wokWithUserInput()
    

def main():
    print("привет введи D для того чтобы я покказал как работает программа\n" \
    "и I для другой работы с программой")
    userInput = input()
    if userInput == "D":
        a = int(input())
        demonstration(a)
    if userInput == "I":
        wokWithUserInput()
    else:
        print("некоректный ввод")
        main()

main()
