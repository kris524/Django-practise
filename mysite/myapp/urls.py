from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('base/', views.base, name = 'base'),
    path('user_info/', views.user_info, name = 'user_info'),
    path("just_form/", views.just_form, name = "just_form"),
    path('<int:id>/data', views.data, name='data')

]