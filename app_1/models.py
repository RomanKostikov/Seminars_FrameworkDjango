# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или
# решка.
# Также запоминайте время броска
# Задание №2
# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.
from django.db import models


# Create your models here.
class Coin(models.Model):
    is_heads = models.BooleanField()
    flip_time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_coin_stats(number: int) -> dict:
        last_flips = Coin.objects.all()[:number]
        flips_stats = {
            'heads': [],
            'tails': []
        }

        for coin in last_flips:
            if coin.is_heads:
                flips_stats['heads'].append(coin.flip_time)
            else:
                flips_stats['tails'].append(coin.flip_time)

        return flips_stats

    def __str__(self):
        return f'Coin flip at {self.flip_time}: heads: {self.is_heads}'


# Задание №3
# Создайте модель Автор. Модель должна содержать
# следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное
# имя”, которое возвращает имя и фамилию.

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return f'Author: {self.name} {self.last_name}, email: {self.email}'


# Задание №4
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию
# False

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post: {self.title}, Author: {self.author}'
