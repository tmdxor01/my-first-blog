from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/self_portrait.html', {})