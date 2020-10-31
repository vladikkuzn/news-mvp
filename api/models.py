from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    creation_date = models.DateTimeField(auto_now_add = True)
    amount_of_upvotes = models.PositiveIntegerField(default = 0)
    author_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author_name = models.CharField(max_length = 200)
    content = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add = True)
    comment_on = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")

