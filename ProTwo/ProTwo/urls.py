

from django.contrib import admin
from django.urls import path
from AppTwo import views
from django.conf.urls import url, include

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^set_meal/', views.meal, name='meal'),
    url(r'^about/',views.about, name='about'),
    url(r'^registration/', views.register, name = 'registration'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^special/', views.special, name='special'),
    url(r'^login/', views.user_login, name='user_login'),
    url(r'^free_meal/', views.free_meal, name='free_meal'),
    url(r'^notifications/', views.notifications, name = 'notifications'),
]
