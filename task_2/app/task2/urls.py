from django.urls import path

from task2.views import index_view, add_view, sub_view, multi_view, divide_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='add'),
    path('subtract/', sub_view, name='subtract'),
    path('multiply/', multi_view, name='multiply'),
    path('divide/', divide_view, name='divide'),
]
