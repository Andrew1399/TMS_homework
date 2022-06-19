from django.db import models
from users.models import Author
from django.contrib.auth.models import User


class Tag(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
      return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Class for writer content.
    """
    title = models.CharField(max_length=120, db_index=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    is_draft = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='blog_post')

    class Meta:
        ordering = ['-created_on']

    def count_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by'.format(self.name)