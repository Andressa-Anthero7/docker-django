from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agradecimento/', views.agradecimento, name='agradicimento'),
    path('accounts/login/<str:user>/dashboard/', views.dashboard, name='dashboard'),
]