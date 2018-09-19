from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('output/', views.output, name='output'),
]
