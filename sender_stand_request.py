import configuration
import requests
import data


# запрос на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # передаем полный путь
                         json=order_body)  # тело запроса


# получение трека заказа
def get_new_track_order():
    # в переменную response сохраняется результат запроса на создание заказа
    response = post_new_order(data.order_body)
    # в track_order response сохраняется значение track
    track_order = response.json()["track"]
    # возвращает значение track
    return track_order


# запрос на получение заказа по треку заказа
def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,  # передаем полный путь
                        params={"t": get_new_track_order()})  # параметр запроса
