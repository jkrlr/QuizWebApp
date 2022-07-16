from django.urls import path

from . import views

app_name = 'quizes'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_question/', views.add_question, name='add_question'),
]
