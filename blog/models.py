from django.db import models
from django_extensions.db.fields import AutoSlugField
from profiles.models import UserProfile

STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    """
    Model for the blog posts
    """
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True,)
    category = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(default='placeholder')
    excerpt = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(UserProfile, related_name='blog_likes', blank=True)

    class Meta:
        """
        Order the posts in descending order.
        """
        ordering = ['-publish_date']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return self.title

    def number_of_likes(self):
        """
        See number of likes on a post.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Add a comment.
    """
    recipe = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order by oldest comment first
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
