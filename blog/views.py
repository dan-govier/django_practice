from django.shortcuts import render

posts = [
    {
        'author': 'DanG',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 15, 2021'
    },
    {
        'author': 'JaneD',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 18, 2021'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')