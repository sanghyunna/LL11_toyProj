import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from guestBook.models import *

# Create your views here.
# @require_http_methods(["GET", "POST", "DELETE"])
def posts(request, id):
    if request.method == "GET":
        post = get_object_or_404(Post, pk = id)
        return_json ={
            "postName" : post.postName,
            "authorId" : post.authorId,
            "authorName" : post.authorName,
            "dateCreated" : post.created_at
        }

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 조회 성공',
            'data' : return_json
        })
    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk=id)
        delete_post.delete()
        return JsonResponse({
            'status' : 200,
            'message' : '게시글 삭제 성공'
        })

def createPost(request):
    body = json.loads(request.body.decode('utf-8'))
    Post.objects.create(
        postName = body['postName'],
        postContent = body['postContent'],
        authorId = body['authorId'],
        authorName = body['authorName'],
    )

    return JsonResponse({
        'status' : 200,
        'message' : 'Success',
    })

def postList(request):
    objects = Post.objects.all()
    res = []
    for obj in objects:
        res.append({
            "dateCreated" : obj.created_at,
            "authorId" : obj.authorId,
            "authorName" : obj.authorName,
            "postName" : obj.postName,
            "postContent" : obj.postContent,
        })
    return JsonResponse({
        'status' : 200,
        'message' : 'Success',
        'data' : res
    })