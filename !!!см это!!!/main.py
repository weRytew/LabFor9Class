from manu import manu
from plenet import planet
from resept2 import resept

def main():
    w = True
    while w:
        print("рецепты или планеты, exti для выхода")
        usinp = input()
        if usinp == "планеты":
            manu("p", planet, "имя;радиус;все;растояние от солнца;тип", "по чему: name/radius/weight/distance from the Sun/type", ["Название", "радиус", "вес", "раст от солнца", "тип"])
        elif usinp == "рецепты":
            manu("r", resept, "имя;категория;время готовки;ингридиенты;сложность", "по чему: name/categoray/timeForCook/ingredients/level", ["Название", "Категория", "время готовки", "ингридиенты", "сложность"])
        # ["Название", "Категория", "время готовки", "ингридиенты", "сложность"]
        elif usinp == "exit":
            w = False
if __name__ == "__main__":
    main()