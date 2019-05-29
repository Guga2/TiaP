import random
n = random.randit(1, 100)
chis = int(input("Угадай число -"))
step = 1
while chis != n:
    if chis > n:
        print ("Не пробил (Меньше)") 
         elif chis < n:
              print ("Не пробил (Больше)")
        chis = int(input("попробый еще раз вдруг получиться"))
        step += 1
        print ("о получилось ты угадал:", num ,"попыток-", step)

