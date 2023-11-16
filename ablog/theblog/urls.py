from django.urls import path

# **from theblog import views

from .views import IndexView, ArticleDetailView
urlpatterns = [
    #Donde index es una funcion a mostrar como template
    # **path('', views.index, name="index"), #Donde index es una funcion a mostrar como template
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
