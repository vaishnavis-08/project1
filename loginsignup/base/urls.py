from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('report-grievance/', views.report_grievance_view, name='report_grievance'), 
    
]