import configuration
import requests
import data

# Функция для создания заказа на основе тела запроса из data.py
def post_new_order() -> requests.Response:
    return requests.post(configuration.URL + configuration.NEW_ORDER, json=data.order_body)


# Функция получения заказа по номеру
def get_order_by_track(track) -> requests.Response:
    return requests.get(configuration.URL + configuration.GET_ORDER, params={'t' : track})