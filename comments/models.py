from django.db import models

from users.models import User

from posts.models import Posting


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')

    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    is_liked = models.ManyToManyField(User, through='UserCommentRelation',
                                      related_name='comments_liked')


    def __str__(self):
        return f'Material: {Posting.title}, Commented By: {self.user}'

class UserCommentRelation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    liked_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Liked By:{self.user}'