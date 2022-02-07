# Дано два списка
# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# Создать из них список кортежей
# list_c = [(1,5), (2,6), (3,7), (4,8)]
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = list(zip(list_a, list_b))
print(list_c)
#
# Дано список
# ["bar", "baz", "qux", "etc"]
# Создать кортеж
# ("foo", "bar", "baz", "qux", "etc")
a = ["bar", "baz", "qux", "etc"]
a.insert(0, "foo")
b = tuple(a)
print(b)
#
# Задано список my_list = (1, 2, 3, 4, 5)
# Получите шестой єлемент списка. В случае его отсутствия отсутствия видайте відайте сообщение о его отсутствии.
my_list = (1, 2, 3, 4, 5)
if (len(my_list) == 6):
    print(my_list[5])
else:
    print("Element not found")
# либо так
my_list = (1, 2, 3, 4, 5)
if(my_list.index(len(my_list)) == 6):
    print(my_list[5])
else:
    print("Element not found")
