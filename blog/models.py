from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
#from django_comments.moderation import CommentModerator
#from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator, SpamModerator
#from blog.badwords import badwords


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


