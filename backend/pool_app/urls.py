from django.urls import path

from .views import index

app_name = 'pool_app'

urlpatterns = [
    path('', index, name='index'),
]