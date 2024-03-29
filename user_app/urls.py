from django.urls import path
from user_app import views


# Template URL

app_name = 'user_app'


urlpatterns = [
    path('register/',views.register, name ='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('special_view/', views.special_view, name='special_view'),
]