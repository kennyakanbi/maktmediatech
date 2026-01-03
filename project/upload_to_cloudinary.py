import os
import django
from cloudinary.uploader import upload

# =======================
# Setup Django
# =======================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from myapp.models import Blog, BlogImage

# =======================
# Upload main blog images
# =======================
for blog in Blog.objects.all():
    if blog.image and not str(blog.image.url).startswith("http"):
        try:
            result = upload(blog.image.path)
            blog.image = result['secure_url']
            blog.save()
            print(f"✅ Uploaded main image for: {blog.title}")
        except Exception as e:
            print(f"❌ Failed to upload main image for {blog.title}: {e}")

# =======================
# Upload extra blog images
# =======================
for extra in BlogImage.objects.all():
    if extra.image and not str(extra.image.url).startswith("http"):
        try:
            result = upload(extra.image.path)
            extra.image = result['secure_url']
            extra.save()
            print(f"✅ Uploaded extra image for: {extra.blog.title}")
        except Exception as e:
            print(f"❌ Failed to upload extra image for {extra.blog.title}: {e}")

print("\nAll done! All local images should now be on Cloudinary.")
