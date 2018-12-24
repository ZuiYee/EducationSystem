from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^regist/', views.regist, name='regist'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^teacherchange/', views.teacherchange, name='teacherchange'),
    url(r'^studentchange/', views.studentchange, name='studentchange'),
    url(r'^studentchangepassword/', views.studentchangepassword, name='studentchangepassword'),
    url(r'^teacherchangepassword/', views.teacherchangepassword, name='teacherchangepassword'),
]
