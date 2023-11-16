from django.shortcuts import render

# Utilizando las vistas genericas de django
# Listview Esta consulta generica trae los posts y los enlista
# DetailView Al dar click nos muestra el post 
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# La funcion index es exportada a urls.py de app
# def index(request):
# 	""" Vista para atender la petición de la url / """
# 	return render(request, "theblog/index.html", {})

# La funcion indexView es exportada a urls.py de app
class IndexView(ListView):
    model = Post
    template_name = 'index.html' 
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'