def ask_user(question):
    while question != 'Хорошо':
        print('что же ты так? Подумай в позитивном ключе!')
        question=input('Как дела? ')
    else:
        print('Ну вот и славненько :3')

ask_user(input('Как дела? '))



