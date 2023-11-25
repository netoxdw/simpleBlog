from django.urls import path

# **from theblog import views

from .views import IndexView, ArticleDetailView, AddPostView, UpdatePostView
urlpatterns = [
    #Donde index es una funcion a mostrar como template
    # **path('', views.index, name="index"), #Donde index es una funcion a mostrar como template
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
]
