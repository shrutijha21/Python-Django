from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.png",
        "author": "Shruti",
        "date": date(2023, 9, 10),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Mountain hiking is a breathtaking adventure that allows us to escape the hustle and bustle of everyday life and connect with the natural world in its most majestic form. 
          The allure of the mountains has drawn adventurers and nature lovers for centuries, and for a good reason.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "Shruti",
        "date": date(2024, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Programming is like a puzzle-solving adventure,
          a journey of turning logic into reality. In this digital age,
          it's a superpower that empowers us to create, automate, and innovate.
          Whether you're a seasoned developer or a curious beginner,
          the world of programming offers endless opportunities for growth and creativity.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.png",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Nature, in all its glory, is a masterpiece that has captivated humanity for millennia.
          From the grandeur of towering mountains to the serenity of a babbling brook, nature's artistry is boundless. 
          Let's take a moment to marvel at some of the most remarkable aspects of our natural world.
        """
    }
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
