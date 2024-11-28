from django.urls import path
from . import views

urlpatterns = [
    path('', views.startup_view, name='startup'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('result/<str:result>/', views.result_view, name='result'),
    path('records/', views.view_records, name='records'),
]
