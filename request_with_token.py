import requests
import json

client_id = '9ff0516e2c6b6c2d4ae9'
client_secret = '54b7dc7ab69c3e652d643e99a1272d98'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаём пустой список для данных из ответного словаря
artists = []

# открываем файл с данными для ввода
with open("dataset_24476_4.txt") as file:
    art_id = [lines.strip() for lines in file]
    for ids in art_id:
        # создаем заголовок, содержащий наш токен
        headers = {"X-Xapp-Token": token}
        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/{}".format(ids), headers=headers)
        r.encoding = 'utf-8'

        # разбираем ответ сервера
        data = json.loads(r.text)
        # ответ - это словарь словарей, добавляем нужные нам ключи-значения
        artists.append({'name': data['sortable_name'], 'birthday': data['birthday']})

# двойная сортировка - год рождения в порядке неубывания и имя в лексикографическом порядке
for artist in sorted(artists, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])