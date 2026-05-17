# Пример бинарного поиска O(log n)
minim = 1
maxim = int(input("Введи максимальное число: "))
print(f"Загадай число в интервале от 1 до {maxim}")
print("Если число больше предпологаемого компьтером то вводи + если меньше то - если компьюте угадал введи =")
attems = 0

while minim <= maxim:
    attems += 1
    mid = (minim + maxim) // 2
    pl = input(f"Твое число больше {mid}?")
    if pl == "+":
        minim = mid+1
    elif pl == "-":
        maxim = mid-1
    elif pl == "=":
        print(f"Попыток {attems}")
        exit()
    else:
        print("Ошибка принамаются только + - =")


print("Ошибка возможно вы ошиблись")