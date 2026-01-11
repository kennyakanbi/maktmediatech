from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, Blog, Internship, BlogImage
from .forms import BlogForm


# =====================
# Contact Admin
# =====================
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "short_message", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

    short_message.short_description = "Message"


# =====================
# Blog Image Inline
# =====================
class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 0  # ❗ Prevent empty inline rows causing 500 errors


# =====================
# Blog Admin
# =====================
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
            "fields": ("title", "slug", "description", "image")
        }),
        ("Author & Time", {
            "fields": ("author_name", "date_created")
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author_name = request.user
        super().save_model(request, obj, form, change)

    def image_preview(self, obj):
        if obj.image:
            try:
                return format_html(
                    '<img src="{}" width="100" style="object-fit: cover;" />',
                    obj.image.url
                )
            except Exception:
                return "Image not available"
        return "No Image"

    image_preview.short_description = "Image"


# =====================
# Internship Admin
# =====================
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
