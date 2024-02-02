from django.urls import path
import app_1.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/', views.coin_flip, name='coin'),
    path('c/', views.coin_stat, name='coin_stat'),
    path('r/', views.random_number, name='random'),
    path('authors/', views.authors_view, name='authors'),
    path('posts/', views.posts_view, name='posts'),
    path('coin_flip_sem_3/<int:count>/', views.coin_flip_sem_3, name='game'),
    path('dice_roll_sem_3/<int:count>/', views.dice_roll_sem_3, name='game'),
    path('random_number_sem_3/<int:count>/', views.random_number_sem_3, name='game'),
    path('author_post/<int:author_id>/', views.authors_view_sem_3, name='author_post'),
    path('post/<int:post_id>/', views.posts_view_sem_3, name='posts_view_sem_3'),
    path('chose_game/', views.chose_game, name='chose_game'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('posts_add/', views.posts_add, name='posts_add'),
]
