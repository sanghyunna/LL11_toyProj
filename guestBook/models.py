from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    postId = models.AutoField(primary_key=True)
    postName = models.CharField(verbose_name="게시물제목", max_length=50)
    authorId = models.BigIntegerField(verbose_name="작성자id")
    authorName = models.CharField(verbose_name="작성자이름", max_length=20)
    postContent = models.CharField(verbose_name="게시물내용", max_length=500)