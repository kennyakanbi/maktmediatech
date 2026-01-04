from myapp.models import Blog

def seed_blogs():
    if Blog.objects.exists():
        return

    Blog.objects.create(
        title="Media Advertising Campaigns — Let the World Notice You",
        content="Your full blog content here...",
        published=True
    )
