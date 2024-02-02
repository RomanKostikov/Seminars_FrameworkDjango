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
from django.shortcuts import render
from .models import Author, Coin, Post
from app_1.forms import GameForm, AuthorForm, PostAddFormWidget

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница',
    }
    logger.info('index get request')
    return render(request, 'app_1/index.html', context)


def about(request):
    context = {
        'name': 'Roman',
    }
    logger.info('about get request')
    return render(request, 'app_1/about.html', context)


def coin_flip(request):
    coin_sides = [True, False]
    coin_sides_str = ['Tails', 'Heads']
    side = choice(coin_sides)
    coin = Coin(is_heads=side)
    coin.save()

    logger.info(f'Coin flipped at side: {coin_sides_str[side]}')
    return HttpResponse(f'<p>Coin side: {coin_sides_str[side]}</p>')


def coin_flip_sem_3(request, count):
    """
    Задание №3
    Доработаем задачу 7 из урока 1, где бросали монетку,
    игральную кость и генерировали случайное число.
    Маршруты могут принимать целое число - количество
    бросков.
    Представления создают список с результатами бросков и
    передают его в контекст шаблона.
    Необходимо создать универсальный шаблон для вывода
    результатов любого из трёх представлений.
    """
    list_result = []
    for i in range(int(count)):
        coin_sides = [True, False]
        coin_sides_str = ['Tails', 'Heads']
        result = choice(coin_sides)
        list_result.append(coin_sides_str[result])
        logger.info(f'Coin flipped at side: {coin_sides_str[result]}')
    context = {
        'title': 'Coin flip',
        'result': list_result,
    }
    return render(request, 'app_1/game.html', context)
    # return HttpResponse(f'<p>Coin result: {coin_sides_str[result]}</p>')


def coin_stat(request):
    coin_flips = Coin.get_coin_stats(10)
    return HttpResponse(str(coin_flips))


def dice_roll(request):
    dice_side = randint(1, 6)

    logger.info(f'Dice side: {dice_side}')
    return HttpResponse(f'<p>Dice side: {dice_side}</p>')


def dice_roll_sem_3(request, count):
    """
    Seminar_3
    :param request:
    :return:
    """
    list_result = []
    for i in range(count):
        dice_side = randint(1, 6)
        list_result.append(dice_side)
        logger.info(f'Dice side: {dice_side}')
    context = {
        'title': 'Dice roll',
        'result': list_result,
    }
    return render(request, 'app_1/game.html', context)


def random_number(request):
    rand_number = randint(0, 100)

    logger.info(f'Random number from 0 to 100: {rand_number}')
    return HttpResponse(f'<p>Random number from 0 to 100: {rand_number}</p>')


def random_number_sem_3(request, count):
    """
    Seminar_3
    :param request:
    :return:
    """
    list_result = []
    for i in range(count):
        rand_number = randint(0, 100)
        list_result.append(rand_number)
        logger.info(f'Random number from 0 to 100: {rand_number}')
    context = {
        'title': 'Random number',
        'result': list_result,
    }
    return render(request, 'app_1/game.html', context)


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


def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)


def posts_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)


def authors_view_sem_3(request, author_id):
    """
    Seminar_3
    :param request:
    :return:
    """
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    print(posts)
    return render(request, 'app_1/author_post.html', {'author': author, 'posts': posts})


def posts_view_sem_3(request, post_id):
    """
    Seminar_3
    :param request:
    :return:
    """
    post = Post.objects.get(id=post_id)
    return render(request, 'app_1/post.html', {'post': post})


# Доработаем задачу 1.
# Создайте представление, которое выводит форму выбора.
# В зависимости от переданных значений представление
# вызывает одно из трёх представлений, созданных на
# прошлом семинаре (если данные прошли проверку, конечно же).
def chose_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            count = form.cleaned_data['count']
            # Делаем что-то с данными
            logger.info(f'Получили {game_type=}, {count=}.')
            if game_type == 'coins':
                return coin_flip_sem_3(request, count)
            elif game_type == 'dice':
                return dice_roll_sem_3(request, count)
            elif game_type == 'random number':
                return random_number_sem_3(request, count)
    else:
        form = GameForm()
    return render(request, 'app_1/games.html', {'form': form})


def authors_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            logger.info(f'Получили {name=}, {email=}, {bio=}, {birthday=}.')
            author = Author(name=name, last_name=last_name, email=email, bio=bio, birthday=birthday)
            author.save()
            message = 'Автор сохранён'
    else:
        form = AuthorForm()
        message = 'Заполните форму'
    return render(request, 'app_1/authors_add.html', {'form': form, 'message': message})

# Аналогично автору создайте форму добавления новой
# статьи.
# Автор статьи должен выбираться из списка (все доступные в
# базе данных авторы).

def posts_add(request):
    if request.method == 'POST':
        form = PostAddFormWidget(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            views = form.cleaned_data['views']
            is_published = form.cleaned_data['is_published']
            logger.info(f'Получили {title=}, {content=}, {publish_date=}, {author=}.')
            post = Post(title=title, content=content, publish_date=publish_date, author=author, category=category,
                        views=views, is_published=is_published)
            post.save()
            message = 'Статья сохранёна'
    else:
        form = PostAddFormWidget()
        message = 'Заполните форму'
    return render(request, 'app_1/posts_add.html', {'form': form, 'message': message})
