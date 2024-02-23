from django.urls import re_path
from user_app import views


# Template URL

app_name = 'user_app'


urlpatterns = [
    re_path(r'^register/',views.register, name ='register'),
    re_path(r'^login/', views.login, name = 'name'),
]