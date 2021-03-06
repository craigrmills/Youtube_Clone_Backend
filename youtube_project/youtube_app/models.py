from django.db import models

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.body

class Reply(models.Model):
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=250)

    def __str__(self):
        return self.body