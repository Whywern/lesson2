classes = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [5,5,5,2,5,5]},
    {'school_class': '4c', 'scores': [4,1,1,5]}
]
x = 0
for sred_school in classes:
    x = x + sum(sred_school['scores']) / len(sred_school['scores'])
    sred_school = x / len(classes)
print(sred_school)
for sred_klass in classes:
    sred_klass = sum(sred_klass['scores']) / len(sred_klass['scores'])
    print (sred_klass)