from django.urls import path

from . import views

urlpatterns = [
    path('polls/', views.index, name='polls-index'),
    path('polls/xablau', views.xablau, name='xablau'),
    path('', views.index, name='index'),
]