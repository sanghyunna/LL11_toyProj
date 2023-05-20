import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from guestBook.models import *

# Create your views here.
# @require_http_methods(["GET", "POST", "DELETE"])
def posts(request, id):
    if request.method == "GET":
        post = get_object_or_404(Post, pk = id)

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 조회 성공',
            "postName" : post.postName,
            "dateCreated" : post.created_at,
            "authorName" : post.authorName,
            "authorId" : post.authorId,
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
    try:
        authorId = body['authorId']
    except KeyError:
        return JsonResponse({
            'status' : 400,
            'message' : 'authorIdError'
        })
    

    try:
        postName = body['postName']
    except KeyError:
        return JsonResponse({
            'status' : 400,
            'message' : 'postNameError'
        })
    

    try:
        postContent = body['postContent']
    except KeyError:
        return JsonResponse({
            'status' : 400,
            'message' : 'postContentError'
        })
    

    try:
        authorName = body['authorName']
    except KeyError:
        return JsonResponse({
            'status' : 400,
            'message' : 'authorNameError'
        })
    
    Post.objects.create(
        authorId = authorId,
        postName = postName,
        postContent = postContent,
        authorName = authorName,
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
            "postId" : obj.postId,
            "dateCreated" : obj.created_at,
            "authorId" : obj.authorId,
            "authorName" : obj.authorName,
            "postName" : obj.postName,
            "postContent" : obj.postContent,
        })
    return JsonResponse({
        "status" : 200,
        "message" : "Success",
        "data" : res
    })