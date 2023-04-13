from django.urls import path

from task1.views import calculation_view

urlpatterns = [
    path('add/', calculation_view, name='add'),
    path('subtract/', calculation_view, name='subtract'),
    path('multiply/', calculation_view, name='multiply'),
    path('divide/', calculation_view, name='divide'),
]