"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(text1,text2):
  if (type(text1) !=str) or (type(text2) != str):
    return '0'
  elif text1==text2:
    return '1'
  elif len(text1) > len(text2):
    return '2'
  elif text1 != text2 and text2 == 'learn':
    return '3'




    
if __name__ == "__main__":
    main(1,2)

print(main('learn', 'math'))
print(main(None, True))
print(main('pull', 'pull'))
print(main('mean', 'learn'))
print(main(9, 'math'))
print(main('learn', 'learn'))


