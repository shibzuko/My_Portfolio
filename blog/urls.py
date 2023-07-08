from django.urls import path, include
from . import views

app_name = 'blog'  # для href="{% url 'blog:detail' post.id %}"

urlpatterns = [
    path('', views.all_blog, name='all_blog'),
    path('<int:blog_id>', views.detail, name='detail'),  # <int:blog_id> автоматически принимает значения

]