choise = input("\n[1] Самостоятельный ввод\n[2] Автовычет\n[3] Подсчёт оценок\n[4] Описание\n: ")
try:
    int(choise)
except:
    print("Это не число. Это печально 😥")
    exit(0)

if choise == "1":
    five = input("\nКол-во пятёрок: "); four = input("Кол-во четвёрок: ")
    three = input("Кол-во троек: "); two = input("Кол-во двоек: ")

    try:
        five = int(five); four = int(four)
        three = int(three);  two = int(two)
    except:
        print("Это не похоже на числа. Это печально 😥")
        exit(0)

    res = (5*five + 4*four + 3*three + 2*two) / (five + four + three + two)
    res = str(res)[:4]
    print (f"Округлённый средний балл: {res}")
    # (5 × n5 + 4 × n4 + 3 × n3 + 2 × n2) / (n5 + n4 + n3 + n2)

elif choise == "2":
    text = input("\nВведите оценки: ").replace(" ", "")
    try:
        text = list(text)
        five = text.count("5"); four = text.count("4")
        three = text.count("3"); two = text.count("2")

        resF = (5*five + 4*four + 3*three + 2*two) / (five + four + three + two)
        res = str(resF)[:4]

        print (f"Округлённый средний балл: {res}")
        print (f"Итоговая оценка: {round(resF)}")

    except:
        print("Это не похоже на числа. Это печально 😥")
        exit(0)

elif choise == "3":
    text = input("\nВведите оценки: ").replace(" ", "")
    try:
        text = list(text)
        print("\nПятёрок: " + str(text.count("5"))); print("Четвёрок: " + str(text.count("4")))
        print("Троек: " + str(text.count("3"))); print("Двоек: " + str(text.count("5")))
    except:
        print("Это не похоже на числа. Это печально 😥")
        exit(0)

elif choise == "4":
    print("""
[1]. Некоторые спросят, зачем нужен этот пункт. \nТак вот... Он нужен что бы прикинуть что нужно сделать что-бы изменить свой средний балл
[2]. Нууу просто вам не надо подсчитывать свои оценки. Вот пример ввода: 4 4 4 3 5 5 4 4 \n(можно и без пробелов. Кстати это - часть моей реальной статистики)
[3]. Подсчёт общего кол-ва двоек, троек и т.п
[4]. Просто описание пунктов. Как вы уже поняли""")

input("press enter, to exit")
