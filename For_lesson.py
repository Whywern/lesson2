#for number in range(5):
#    print(f'Ваше число = {number}!')

#for letter in 'Перпендикулёз':
 #   print(letter.upper())

#string = "Я так до сих пор ничего и не понял ..."
#for word in string.split():
#    print(f'Длинна "{word}": {len(word)}')

numbers = [1, 4, 14, 41, 56, 23, 17]

print(f'средняя цифра = {sum(numbers)/len(numbers)}') 

summa = 0
for srednyaya in numbers:
    summa += srednyaya
    print(summa)

print(f'средняя цифра: {summa/len(numbers)}') 
