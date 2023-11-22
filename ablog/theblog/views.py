from django.shortcuts import render

# Utilizando las vistas genericas de django
# Listview Esta consulta generica trae los posts y los enlista
# DetailView Al dar click nos muestra el post 
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
# Create your views here.


# La funcion indexView es exportada a urls.py de app
class IndexView(ListView):
    model = Post
    template_name = 'index.html' 
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'