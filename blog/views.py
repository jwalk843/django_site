from django.shortcuts import render
from .models import Post
# Create your views here.

# create dummy data here first before making database

posts = [ 
    {
        'author': 'Jay',
        'title': 'Favorite Show',
        'content': 'I love Family Guy!\nStewie cracks me the fuck up lmao :)',
        'date_posted': 'July 26, 2021'
    },

    {
        'author': 'Oscar',
        'title': 'Least Favorite show',
        'content': 'American Dad, it\'s stupid',
        'date_posted': 'July 25, 2021'
    }
]

def home(request):
    context = {
        # key    # posts we created above
        'posts': Post.objects.all()
    }
    # passing in our data we created above to the html template
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
