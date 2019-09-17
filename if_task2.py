comparsion('a', 4)
comparsion('a', 'a')
comparsion('abbbbb', 'a')
comparsion('a', 'learn')
def comparsion (a, b):
    if type(a) != str or type(b) != str:
        print(0)
    elif a == b:
        print(1)
    elif len(a) > len(b):
        print(2)
    elif a != b and b == 'learn':
        print(3)
