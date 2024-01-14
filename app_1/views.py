# Задание №4
# � Создайте представление “Привет, мир!” внутри вашего
# первого приложения.
# � Настройте маршруты

# Задание №5
# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
# � Пропишите маршруты

# Задание №6
# � Добавьте логирование в проект.
# � Настройте возможность вывода в файл и в терминал.
# � Устраните возможные ошибки.
# � *Форматирование настройте по своему желанию.
# Объясните что вы выводите в логи
# + в конце файла settings.py добавляем настройки логирования

# Задание №7
# � Доработайте задачи 5 и 6.
# � Сохраняйте в логи значения, которые генерирует каждое из
# представлений.
# from django.shortcuts import render
import logging
from random import randint, choice
from django.http import HttpResponse

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return HttpResponse("Привет, мир!")


def random_view(request):
    coin_sides = ['Heads', 'Tails']
    dice_side = randint(1, 6)
    rand_number = randint(0, 100)
    logger.info(f'Dice side: {dice_side}')
    logger.info(f'Random number from 0 to 100: {rand_number}')

    return HttpResponse(
        f'<p>Coin side: {choice(coin_sides)}</p><br>\
<p>Dice side: {dice_side}</p><br><p>Random number from 0 to 100: {rand_number}</p>'
    )
