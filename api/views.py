from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer

from .models import Post, Comment
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All posts': '/posts/',
        'Create post': '/post-create/',
        'Detail view post': '/post-detail/<str:pk>/',
        'Update post': '/post-update/<str:pk>/',
        'Delete post': '/post-delete/<str:pk>/',
        'Upvote post': '/post-upvote/<str:pk>/',
        'Reset posts': '/posts-reset/',

        'All comments': '/comments/<str:pk>/',
        'Create comment': '/comment-create/',
        'Detail view comment': '/comment-detail/<str:pk>/',
        'Update comment': '/comment-update/<str:pk>/',
        'Delete comment': '/comment-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all().order_by('-creation_date')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response('Post succsesfully deleted!')

@api_view(['POST'])
def postUpvote(request, pk):
    post = Post.objects.get(id=pk)
    post.amount_of_upvotes += 1
    post.save(update_fields=["amount_of_upvotes"])
    return Response('Post succsesfully upvoted!')

@api_view(['GET'])
def commentList(request, pk):
    comments = Comment.objects.filter(comment_on=pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def commentCreate(request):
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def commentDetail(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def commentUpdate(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def commentDelete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response('Comment succsesfully deleted!')