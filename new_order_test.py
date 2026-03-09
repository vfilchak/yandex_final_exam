# Фильчак Виктория, 41-я когорта — Финальный проект. Инженер по тестированию плюс
import new_order_request as order


def test_new_order():
    # Выполнить запрос на создание заказа
    new_order_request = order.post_new_order()

    # Сохранить номер трека заказа
    track_number = new_order_request.json()['track']

    # Выполнить запрос на получение заказа по треку заказа
    get_order_request = order.get_order_by_track(track_number)
 
    # Проверить, что код ответа равен 200
    assert get_order_request.status_code == 200