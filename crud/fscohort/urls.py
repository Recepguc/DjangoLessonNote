from django.urls import path
from .views import index, student_add, student_list, student_add, student_update

urlpatterns = [
    path('', index, name='home'),
    path('List/', student_list, name='student_list'),
    path('add/', student_add, name='student_add'),
    path('update/<int:id>', student_update, name='student_update'),
]
