from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/detail/<int:id>/', views.post_detail, name='detail'),
    path('add_post', views.add_post, name='add_post'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),

    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]