from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/likes/', views.likes, name='likes'),
    # 2. urls.py에 경로 지정
    path('<int:id>/', views.detail, name='detail'),
    path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/comments/<int:id>/delete/', views.comment_delete, name='comment_delete'),
    #20231114 수업
    path('<int:id>/likes-async/', views.likes_async, name='likes_async')
]