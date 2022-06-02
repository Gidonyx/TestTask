# -*- coding: utf-8 -*-
import requests

arr=[]
url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url).json() #получаем json

for i in range(2):
    for word in response[i]['title'].split(' '):#парсим данные из title
        arr.append(word)#Добавляем в список слова

arr.sort()#Сортируем по алфавиту

for i in arr:#Выводим
    print(i)