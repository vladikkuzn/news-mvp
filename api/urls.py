from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('posts/', views.postList, name="posts"),
    path('post-create/', views.postCreate, name="post-create"),
    path('post-detail/<str:pk>/', views.postDetail, name="post-detail"),
    path('post-update/<str:pk>/', views.postUpdate, name="post-update"),
    path('post-delete/<str:pk>/', views.postDelete, name="post-delete"),
    path('post-upvote/<str:pk>/', views.postUpvote, name="post-upvote"),

    path('comments/<str:pk>/', views.commentList, name="comments"),
    path('comment-create/', views.commentCreate, name="comment-create"),
    path('comment-detail/<str:pk>/', views.commentDetail, name="comment-detail"),
    path('comment-update/<str:pk>/', views.commentUpdate, name="comment-update"),
    path('comment-delete/<str:pk>/', views.commentDelete, name="comment-delete"),
]