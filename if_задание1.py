def age(num):
    if num <= 6:
        return 'детский сад'
    elif num <= 17:
        return 'школа'
    elif num <= 22:
        return 'институт'
    elif num <= 64:
        return 'работа'
    elif num >= 65:
        return 'пенсия'
num = int(input('Укажите Ваш возраст: '))
print(age(num))