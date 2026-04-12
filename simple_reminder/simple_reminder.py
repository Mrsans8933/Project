import time
import winsound
try:
    print("Привет, я твоя напоминалка! что напомнить?")
    reason = input()
    print("Через сколько напомнить?(В секундах)")
    print("P.S 1 час = 3600 секунд")
    timer = int(input())
    print("Отсчет пошел!")
    time.sleep(timer)
    print("Напоминание: ", reason)
    for i in range(3):
        winsound.Beep(1000, 100)
        time.sleep(0.3)
except:
    print("Ошибка, возможно вы не ввели время")
