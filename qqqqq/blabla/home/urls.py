from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'homepage'),
    path('other/', other, name='otherpage'),
    path('other1/', other1, name='other1page'),
    path('other2/', other2, name='other2page'),
    path('other3/', other2, name='other3page'),
    
]
