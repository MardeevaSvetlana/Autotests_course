# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open("test_file/task3.txt", "r") as file:  # открыли файл на чтение
    purch_data = file.read().strip().split("\n\n")  # сформировали список со всеми покупками, убрав '\n'


purchases = []
for purchase in purch_data:  # итерируемся по списку, создавая новый список, в который добавляем суммы
    purchase_list = []
    for price in purchase.split("\n"):
        purchase_list.append(int(price))
    purchases.append(purchase_list)  # формируем список списков


sum_list = [sum(sublist) for sublist in purchases]  # итерируемся по списку списков,
# добавляя в новый список суммы всех покупок

three_most_expensive_purchases = sum(sorted(sum_list, reverse=True)[:3])  # сортируем список сумм по возрастанию,
# суммируем три максимальные суммы

assert three_most_expensive_purchases == 202346
