from django.urls import path
from blog.views import (
    BlogList,
)


urlpatterns = [
    path('', BlogList.as_view(), name='blog'),
]
