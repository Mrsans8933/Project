count_of_number = []
divider = 0
new_num = str()
summ = 0
print("Введи число, или Stop для подсчета")
while True:
    try:
        inputnum = input()
        new_num = inputnum
        inputnum = float(inputnum)
        count_of_number.append(inputnum)
        divider += 1
        summ += inputnum
    except:
        if new_num == "Stop" or new_num == "stop":
            break
try:
    print("Среднее арифметическое:", summ / divider)
    print("Введеные числа: ", *count_of_number)
except:
    print("Ошибка, похоже вы не ввели числа")