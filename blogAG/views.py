from django.shortcuts import render


def post_list(request):

    return render(request, 'blogAG/post_list.html', {})
