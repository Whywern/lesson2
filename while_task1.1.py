slovar = {"Как дела?": "Так себе...", "Что делаешь?": "Программирую", "Как настроение?": "Паршивенько", "Что по погоде?": "Неважнецкая", "Чего так?": "Всё не так!"}

def ask_user():
    x = 'Спрашивай...\n'
    while True:
        ask_user = input(x)
        if ask_user not in slovar:
            x = 'Попробуй ещё...\n'
            print('Не знаю, как ответить на: ', ask_user)
        else:
            x = 'Чего ещё?\n'
            print(slovar[ask_user])
ask_user()