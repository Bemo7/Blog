from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="startign_page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug>", views.post_info, name="post-info-page")
]
