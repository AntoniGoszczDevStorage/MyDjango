from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import DetailView
from django.views.generic import TemplateView


class Image(TemplateView):

    form = PostForm
    template_name = 'blogAG/image.html'

    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk':obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):

        return self.post(request, *args, **kwargs)


class ImageDisplay(DetailView):

    model = Post
    template_name = 'blogAG/image_display.html'
    context_object_name = 'image'

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blogAG/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogAG/post_detail.html', {'post': post})

def error_404_view(request, exception):
    data = {"name":'Cos nie dziala'}
    return render(request, 'blogAG/404.html', data)

def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)

    else:

        form = PostForm()

    return render(request, 'blogAG/post_edit.html', {'form': form})

def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)

    else:

        form = PostForm(instance=post)

    return render(request, 'blogAG/post_edit.html', {'form': form})
