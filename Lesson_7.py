 # 1. Рассмотреть метод sort (https://www.w3schools.com/python/python_lists_sort.asp) проработать сделать свои примеры
list = ["48", "50", "12", "38", "45"]
list.sort()
print(list)

list = ['cat', 'dog', 'chiken', 'duck']
list.sort()
print(list)

list = ['cat', 'dog', 'chiken', 'duck']
list.sort(reverse = True)
print(list)

# 2. Реализовать копирование списков через “spred” оператор, и конструктор list() проверить id
fruits = ['apple', 'banana', 'melon', 'pineapple', {1,2,3}, {1:2, 2:3, 3:4}, [1,2,3,4]]
fr = fruits.copy()
print(fr)
print(fruits)
print(id(fr))
print(id(fruits))

fruits = ['apple', 'banana', 'melon', 'pineapple', {1,2,3}, {1:2, 2:3, 3:4}, [1,2,3,4]]
fr = list(fruits)
print(fr)
print(id(fr))
print(id(fruits))

# 3. Задана строка “sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;” создать список которий содержит только цифри.
a = "sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;"
b = [int(i) for i in a if '0'<=i<='9']
print(b)

# 4. Зада список [121, 544, 111, 99, 77] создать список элементи которого деляться на 11.
# вариант 1
list = [121, 544, 111, 99, 77]
newlist = []
for x in list:
  if x%11 == 0:
    newlist.append(x)
print(newlist)

# вариант 2
list = [121, 544, 111, 99, 77]
newlist = [x for x in list if x % 11 == 0]
print(newlist)

# 5. Имеется начальный список цен на изделия. Сегодня на них дана скидка 10 %. Составить новый с учетом удешевления стоимости.
list = [65, 78, 15, 25, 120]
sale = 0.10
newlist = [int(x * (1 - sale)) for x in list]
print(newlist)

# 6. Задан список фруктов ['apple', ‘pear’, 'banana', 'melon', 'pineapple'] создать список если слово начинаеться букви “р”, добавить до слова “my ”. Нужно получить такой список ['my pear', 'my pineapple'].
fruits = ['apple', 'pear', 'banana', 'melon', 'pineapple']
new_fruits = [s for s in fruits if s[0] == 'p']
print(new_fruits)
# никак не додумаюсь, как добавить "my"
