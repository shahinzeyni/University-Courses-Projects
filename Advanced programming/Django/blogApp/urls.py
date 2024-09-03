from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles),
    path('<str:slug>/', views.single_article),

]