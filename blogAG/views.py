from .models import Post
from django.shortcuts import render
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blogAG/post_list.html', {'posts': posts})
