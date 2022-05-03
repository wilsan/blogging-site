from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.


def starting_page(request):
    # # sort posts by the 'date' key in each post
    # sorted_posts = sorted(all_posts, key=get_date)
    # # get the latest 3 posts from sorted_posts
    # latest_posts = sorted_posts[-3:]

    latest_posts = Post.objects.all().order_by('-date')[:3]  # see notes2.txt for details
    return render(request, 'blog/index.html', {  # passing the context to render()
        'posts': latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    # identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)  # same as above, but raises 404 if Post not found
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })
