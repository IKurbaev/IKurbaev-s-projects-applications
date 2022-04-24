# Весь код программы
def main():
    while True:
        # Вывод титульной строки
        print("Программа \"Калькулятор программиста\".")
        # Вывод меню выбора функций
        print("""
            1 - Функция перевода из десятичной системы в двоичную.
            2 - Функция перевода из десятичной системы в восьмеричную.
            3 - Выход из Программы
            """)
        select_input = int(input("Ваш выбор:"))
        if select_input == 1:
            from_dec_to_bin()
        if select_input == 2:
            from_dec_to_octo()
        if select_input == 3:
            break
        else:
            print("В меню нет пункта", select_input)
    input("Нажмите Enter...")

def from_dec_to_bin():
    '''Из десятичной в двоичную систему'''
    x = int(input("Введите целое число:"))
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    print(n)

def from_dec_to_octo():
    '''Из десятичной в восьмеричную систему'''
    x = int(input("Введите целое число:"))
    n = ""
    while x > 0:
        y = str(x % 8)
        n = y + n
        x = int(x / 8)
    print(n)
def from_bin_to_dec():
    x = int(input("Введите двоичное число: "))
    

# Start
main()