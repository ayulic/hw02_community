from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


# Главная страница
def index(request):
    # template's url
    template = 'posts/index.html'
    # page title
    title = "Yatube: Main Page"
    text = 'Yatube: Последние обновления на сайте'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # data dictionary
    context = {
        'title': title,
        'text': text,
        'posts':posts
    }
    # return HttpResponse(f'Main page (index.html)')
    return render(request, template, context)


def group_posts(request, slug):
    # template = 'posts/group_list.html'
    # # page title
    title = f"Записи сообщества {slug}"
    text = f"Записи сообщества {slug}"
    # # data dictionary
    # context = {
    #     'title': title,
    #     'text':text
    # }

    # return render(request, template, context)
        # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    template = 'posts/group_list.html'

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': text,        
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context) 




# def user(request, name):
#     return HttpResponse(f"{str(name).capitalize()}'s Posts")

