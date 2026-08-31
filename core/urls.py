from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('comment/', views.add_site_comment, name='add_site_comment'),
]