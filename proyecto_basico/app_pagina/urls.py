from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pagina1/', views.pagina1, name='pagina1'),
    path('login/', views.login_view, name='login'),
]
