from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # импорт правил из приложения posts
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
