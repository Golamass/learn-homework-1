"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
stock = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
]


def sum_sold(items_sold):
	sum_item = 0
	for items in items_sold:
		sum_item += items
	return sum_item
  

for product in stock:
	sold_result = sum_sold(product['items_sold'])
	print(f'Cуммарное количество продаж для товара {product["product"]}: {sold_result}')

for product in stock:
	avg_result = sum_sold(product['items_sold'])/len(product['items_sold'])
	print(f'Среднее количество продаж для товара {product["product"]}: {avg_result}')
    
total_sold = 0 
for product in stock:
	sold_result = sum_sold(product['items_sold'])
	total_sold += sold_result
print(f'Cуммарное количество продаж: {total_sold}')

total_items=0
for product in stock:
	total_items += len(product['items_sold'])  
print(f'Cреднее количество продаж всех товаров: {total_sold/total_items}')

