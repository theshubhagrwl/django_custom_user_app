from django.urls import path ,include
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('register_data', views.register_data),
    path('logout', views.logout_view),
    path('accounts/profile/', views.dashboard),

]