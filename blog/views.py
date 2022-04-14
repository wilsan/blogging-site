from datetime import date
from django.shortcuts import render

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Wilson George',
        'date': date(2022, 4, 14),
        'title': 'Mountain Hiking',
        'excerpt': """
            There's nothing like the views you get when hiking in the mountains!
            And I wasn't prepared for what happened whilst I was enjoying the view!
            """,
        'content': """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque itaque accusamus sapiente quod, 
            ipsa ab est. Ducimus, modi aut, commodi deserunt minus iure assumenda velit eveniet quia labore 
            nam delectus?

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem nesciunt doloremque laudantium 
            necessitatibus odio officiis accusantium aperiam. Similique cupiditate rem suscipit sint, hic dolor, 
            quis quo expedita porro perferendis consectetur!

            Praesentium veritatis corrupti, dolorum sequi aut laborum, eaque obcaecati dicta reiciendis tempore, 
            asperiores tempora minus hic in impedit ad voluptas laboriosam veniam assumenda pariatur? Qui, quas. 
            Natus beatae iste similique!
            """
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.jpg',
        'author': 'Wilson George',
        'date': date(2022, 2, 14),
        'title': 'Programming Is Great',
        'excerpt': """
            Did you ever spend hours searching that one error in your code? 
            Yep - that's what happened to me yesterday...
            """,
        'content': """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque itaque accusamus sapiente quod, 
            ipsa ab est. Ducimus, modi aut, commodi deserunt minus iure assumenda velit eveniet quia labore 
            nam delectus?

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem nesciunt doloremque laudantium 
            necessitatibus odio officiis accusantium aperiam. Similique cupiditate rem suscipit sint, hic dolor, 
            quis quo expedita porro perferendis consectetur!

            Praesentium veritatis corrupti, dolorum sequi aut laborum, eaque obcaecati dicta reiciendis tempore, 
            asperiores tempora minus hic in impedit ad voluptas laboriosam veniam assumenda pariatur? Qui, quas. 
            Natus beatae iste similique!
            """
    },
    {
        'slug': 'into-the-woods',
        'image': 'woods.jpg',
        'author': 'Wilson George',
        'date': date(2022, 1, 10),
        'title': 'Nature At Its Best',
        'excerpt': """
            Nature is amazing! The amount of inspiration I get when walking in nature is incredible!
            """,
        'content': """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque itaque accusamus sapiente quod, 
            ipsa ab est. Ducimus, modi aut, commodi deserunt minus iure assumenda velit eveniet quia labore 
            nam delectus?

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem nesciunt doloremque laudantium 
            necessitatibus odio officiis accusantium aperiam. Similique cupiditate rem suscipit sint, hic dolor, 
            quis quo expedita porro perferendis consectetur!

            Praesentium veritatis corrupti, dolorum sequi aut laborum, eaque obcaecati dicta reiciendis tempore, 
            asperiores tempora minus hic in impedit ad voluptas laboriosam veniam assumenda pariatur? Qui, quas. 
            Natus beatae iste similique!
            """
    }
]

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)  # sort posts by the 'date' key in each post
    latest_posts = sorted_posts[-3:]  # get the latest 3 posts from sorted_posts
    return render(request, 'blog/index.html', {  # passing the context to render() 
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
