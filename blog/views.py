from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import BlogPost


class BlogList(generic.ListView):
    """
    Creates the recipe list
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-publish_date')
    template_name = 'blog/blog.html'
    paginate_by = 6

