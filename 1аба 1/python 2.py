import random
rnd = random.randint(0,100)

a = False
while a == False:
    chislo = int(input('Угадай число - '))
    if rnd == chislo:
        print('Поздравляем! Вы Выиграли!')
        a = True
    else:
        if chislo < rnd:
            print('больше этого числа !')
        else:
            print('меньше этого числа!')
            