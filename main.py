
def help() -> None:

    print("""
[1]. Автоматически высчитывает средний балл
[2]. Подсчёт общего кол-ва двоек, троек и т.п
[3]. Просто описание""")

def get_marks() -> tuple:

    text = list(input("\nВведите оценки: ").replace(" ", ""))

    five = text.count("5")
    four = text.count("4")
    three = text.count("3")
    two = text.count("2")

    return five, four, three, two

def calculate_marks(marks) -> None: 

    five = marks[0]
    four = marks[1]
    three = marks[2]
    two = marks[3]

    res = str((5 * five + 4 * four + 3 * three + 2 * two) / (five + four + three + two))[:4]
    print(f"Средний балл: {res}")
    print(f"Итоговая оценка: {round(float(res))}")
    
def count_marks(marks) -> None:
    
    five = marks[0]
    four = marks[1]
    three = marks[2]
    two = marks[3]

    print(f"""\nПятёрок: {five}
Четвёрок: {four}
Троек: {three}
Двоек: {two}""")

# выбор действия
def main(choice) -> None:

    match choice:
        
        case 1:

            marks = get_marks()
            calculate_marks(marks)

            input("\npress enter")
        
        case 2:

            marks = get_marks()
            count_marks(marks)

            input("\npress enter")
        
        case 3:

            help()

            input("\npress enter")

# бесконечное меню выбора и ошибок
if __name__ == '__main__':

    while True:

        print("\n"*3)

        try:

            choice = input("[1] Автовычет\n[2] Подсчёт оценок\n[3] Описание\n: ")
            choice = int(choice)

            main(choice)

        except ValueError:
            print("Это похоже не цифры.")

        except ZeroDivisionError:
            print("Либо ты абсолютный счастливчик, либо время ещё не пришло")

        except KeyboardInterrupt:

            print('Пока!')
            break

        except Exception as e:

            print(f'Ошибка: \n{e}')
            break
