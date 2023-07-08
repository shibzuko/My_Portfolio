from django.shortcuts import render, get_object_or_404
from .models import Post

def all_blog(request):
    posts = Post.objects.order_by('-date_time') # order_by('-date_time'), где date_time это поле таблицы. упорядочивает посты по дате
    return render(request, 'blog/all_blog.html', {'posts': posts})


def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)  # kp - Primary Key - для обращение к базе данных по первичному ключу
    return render(request, 'blog/detail.html', {'post': post})








