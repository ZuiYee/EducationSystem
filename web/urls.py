from django.conf.urls import url
from . import views

app_name = 'web'

urlpatterns = [
    url(r'^studentProfile/', views.studentProfile, name='studentProfile'),
    url(r'^teacherProfile/', views.teacherProfile, name='teacherProfile'),
    url(r'^studentparseresult/', views.studentparseresult, name='studentparseresult'),
    url(r'^teacherparseresult/', views.teacherparseresult, name='teacherparseresult'),
]