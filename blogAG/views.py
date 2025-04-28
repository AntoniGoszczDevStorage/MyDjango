from .models import Post
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blogAG/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogAG/post_detail.html', {'post': post})