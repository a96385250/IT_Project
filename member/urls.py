from django.urls import path
from .import views

app_name = 'member'
urlpatterns = [
     path('create',views.create,name='create'),
     path('read',views.read,name='read'),
     path('checkRedis',views.checkRedis,name='checkRedis')
]
