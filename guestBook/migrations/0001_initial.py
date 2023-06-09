# Generated by Django 4.2.1 on 2023-05-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('postName', models.CharField(max_length=50, verbose_name='게시물제목')),
                ('authorId', models.BigIntegerField(max_length=20, verbose_name='작성자id')),
                ('authorName', models.CharField(max_length=20, verbose_name='작성자이름')),
                ('postContent', models.CharField(max_length=500, verbose_name='게시물내용')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
