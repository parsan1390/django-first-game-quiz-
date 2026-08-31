from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('<int:pk>/play/', views.quiz_play, name='quiz_play'),
    path('result/<int:pk>/', views.quiz_result, name='quiz_result'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/like/', views.toggle_like, name='toggle_like'),
]