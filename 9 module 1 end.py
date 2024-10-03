# lst список
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
one = sum(grades[0]) / len(grades[0])
two = sum(grades[1]) / len(grades[1])
three = sum(grades[2]) / len(grades[2])
four = sum(grades[3]) / len(grades[3])
five = sum(grades[4]) / len(grades[4])
# print(one, two, three, four, five)
list1 = (one, two, three, four, five)

# set множества
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st1 = ('Aeron')
st2 = ('Bilbo')
st3 = ('Johhny')
st4 = ('Khendrik')
st5 = ('Steve')
# print(st1, st2, st3, st4, st5)
list2 = (st1, st2, st3, st4, st5)

Dictionary = zip(list2, list1)
print(dict(Dictionary))
