from django.urls import path, include
from ThePass import views

app_name = "ThePass"

urlpatterns = [
    # path('home', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
]