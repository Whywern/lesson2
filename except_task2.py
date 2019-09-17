def discounted(price, discount, max_discount=20):
    try:
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except TypeError:
        print('нет такой буквы в этой цифре')

print(discounted(50000, 20))
print(discounted(50000, 2))
print(discounted('пятихан', 2))
print(discounted(5010, 2))
print(discounted(50000, 'дай скидку'))

