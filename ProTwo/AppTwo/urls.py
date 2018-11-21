from django.urls import path
from AppTwo import views
from django.conf.urls import url

app_name = 'AppTwo'
urlpatterns = [

path('login/', views.user_login, name='user_login'),

]
