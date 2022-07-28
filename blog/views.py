from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import BlogPost
from .forms import CommentForm
from profiles.models import UserProfile


class BlogList(generic.ListView):
    """
    Creates the blog post list
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-publish_date')
    template_name = 'blog/blog.html'
    paginate_by = 6


class BlogDetail(View):
    """
    Class for single log post view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Creates view for a single blog post
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
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Creates view for a comments
        """
        queryset = BlogPost.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by('created_on')
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    """
    Like a blog post
    """
    def post(self, request, slug):
        """
        Change view
        """
        blog = get_object_or_404(BlogPost, slug=slug)
        user = get_object_or_404(UserProfile, user=request.user)
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(user)
        else:
            blog.likes.add(user)

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))
