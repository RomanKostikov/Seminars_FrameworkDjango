# Доработаем задачу про броски монеты, игральной кости и
# случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости,
# числа.
# Второе поле предлагает указать количество попыток от 1 до 64.


from django import forms
from .models import Author, Coin, Post
import datetime


class GameForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('coins', 'Монета'), ('dice', 'Кости'),
                                           ('random number', 'Случайное число')])
    count = forms.IntegerField(min_value=1, max_value=64)


# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу
# данных.
# Используйте ранее созданную модель Author

# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     bio = forms.CharField()
#     birthday = forms.DateField(initial=datetime.date.today)
class AuthorForm(forms.ModelForm):
    """
    Наследование формы от моделей
    """

    class Meta:
        model = Author
        fields = ['name', 'last_name', 'email', 'bio', 'birthday']


# Аналогично автору создайте форму добавления новой
# статьи.
# Автор статьи должен выбираться из списка (все доступные в
# базе данных авторы).

# class PostAddFormWidget(forms.Form):
#     title = forms.CharField(max_length=50,
#                             widget=forms.TextInput(attrs={'class': 'form-control',
#                                                           'placeholder': 'Введите заголовок статьи'}))
#     content = forms.CharField(max_length=150,
#                               widget=forms.TextInput(attrs={'class': 'form-control',
#                                                             'placeholder': 'Введите текст статьи'}))
#     publish_date = forms.DateTimeField(initial=datetime.datetime.now,
#                                        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     author = forms.ModelChoiceField(queryset=Author.objects.all())
#     category = forms.CharField(max_length=100)
#     views = forms.IntegerField(initial=0)
#     is_published = forms.BooleanField(required=False,
#                                       widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class PostAddFormWidget(forms.ModelForm):
    """
    Наследование формы от моделей
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'views', 'is_published']

    publish_date = forms.DateTimeField(initial=datetime.datetime.now,
                                       widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
