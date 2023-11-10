# Кира Шустрова, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


# Тест 1. Успешное получения заказа по треку заказа

def test_can_receive_order_by_track_success_response():
    # В переменную order_response сохраняется результат запроса на получение заказа по треку
    order_response = sender_stand_request.get_order_by_track()
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
