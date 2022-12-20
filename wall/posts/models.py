from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    delete = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

