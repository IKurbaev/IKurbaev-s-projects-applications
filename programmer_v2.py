# Весь код программы
def main():
    while True:
        # Вывод титульной строки
        print("Программа \"Калькулятор программиста\".")
        # Вывод меню выбора функций
        print("""
            1 - Функция перевода из десятичной системы в двоичную.
            2 - Функция перевода из десятичной системы в восьмеричную.
            3 - Функция перевода из двоичной системы в десятичной
            4 - Выход из программы
            """)
        select_input = int(input("Ваш выбор:"))
        if select_input == 1:
            from_dec_to_bin()
        elif select_input == 2:
            from_dec_to_octo()
        elif select_input == 3:
            from_bin_to_dec()
        elif select_input == 4:
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
    bin_num = input("Введите двоичное число: ")
    index = 0
    part_num = 0
    num = 0
    real_index = len(bin_num)
    index_num = len(bin_num) - 1
    for bit in bin_num:
        if index < real_index:
            part_num = int(bit) * (2**index_num)
            index_num -= 1
            index += 1
            num += part_num
    print(num)

# Start
main()