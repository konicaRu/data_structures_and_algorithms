#https://wttr.in/:help?lang=ru
import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '', 'T': '', 'M':'', 'lang':'ru'
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

response = requests.get(url, params=weather_parameters)# передайте параметры в http-запрос

print(response.text)