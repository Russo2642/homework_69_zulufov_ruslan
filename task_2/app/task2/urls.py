from django.urls import path

from task2.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]
