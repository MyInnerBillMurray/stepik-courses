import requests

with open("dataset_24476_3.txt") as file:
    numbers = [lines.strip() for lines in file]

for number in numbers:
    api_url = 'http://numbersapi.com/{}/math?json=true'.format(number)
    params = {
        "default": "Boring number is boring",
    }

    res = requests.get(api_url, params=params)
    data = res.json()
    if data["found"] is True:
        print("Interesting")
    else:
        print("Boring")



# params - словарь параметров запроса, какие нужны.
# В API можно посмотреть словари параметров ответа (res), к ним надо обращаться в формате json.