import random
def common_elements():
    lst3 = lst1.intersection(lst2)
    print(lst3)
lst1 = set(list(random.randrange(3, 69, 3) for i in range(random.randint(0, 100))))
print(lst1)
lst2 = set(list(random.randrange(5, 95, 5) for i in range(random.randint(0, 100))))
print(lst2)
common_elements()