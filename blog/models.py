from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super(Category, self).save()

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blog')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_blog', blank=True)
    #tags = models.ManyToManyField(Tag, blank=True, related_name='tag_blog')
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)
    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    blog_image = models.ImageField(upload_to='blog_images')
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super(Blog, self).save()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='user_blog')
    text = models.TextField(verbose_name='Share your experience')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
class Replay_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_replies')
    blog = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='coment_reply')
    text = models.TextField(verbose_name='Replay')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="liked_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker_user")
