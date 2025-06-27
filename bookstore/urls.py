from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('new_model/', views.new_model_list, name='new_model_list')
]
