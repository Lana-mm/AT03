import requests

def get_random_cat_image():
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        response.raise_for_status()  # Поднимает исключение для кода ошибки HTTP
        data = response.json()
        return data[0]['url'] if data else None
    except requests.exceptions.HTTPError as err:
        return None