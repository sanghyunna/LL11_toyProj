from django.urls import path
from guestBook.views import *

urlpatterns = [
    path('createPost', createPost, name='createPost'),
    path('posts/<int:id>', posts, name='posts'),
    path('postList', postList, name='postList'),
]
# <int:pk> 는 int 값을 받고 그걸 pk에 넘긴다는 뜻