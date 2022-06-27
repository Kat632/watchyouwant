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


class BlogDetail(View):
    """
    Class for single recipe view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Creates view for a single recipe
        """
        queryset = BlogPost.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by('created_on')
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": False,
                "liked": liked,
            },
        )
