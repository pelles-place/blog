from django.contrib import admin
from blog.models import Post, Tag, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )

    prepopulated_fields = {    # dict of string and tuple
        "slug": (
            "title",
            "subtitle",
        )
    }

    date_hierarchy = "publish_date"
    save_on_top = True
