from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, Blog, Internship, BlogImage
from .forms import BlogForm


# -----------------
# Contact Admin
# -----------------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "short_message", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

    short_message.short_description = "Message"


# -----------------
# Blog Images Inline
# -----------------
class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1


# -----------------
# Blog Admin (ONLY ONE)
# -----------------
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author_name", "date_created", "image_preview")
    list_filter = ("date_created",)
    search_fields = ("title", "description")
    readonly_fields = ("date_created",)
    inlines = [BlogImageInline]

    fieldsets = (
        (None, {
            "fields": ("title", "slug", "author_name", "description", "image")
        }),
        ("Timestamps", {
            "fields": ("date_created",)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" style="object-fit: cover;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Image"


# -----------------
# Internship Admin
# -----------------
@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = (
        "fullname",
        "usn",
        "email",
        "college_name",
        "offer_status",
        "start_date",
        "end_date",
        "timeStamp",
    )
    search_fields = ("fullname", "usn", "email", "college_name")
    list_filter = ("offer_status", "college_name", "timeStamp")
