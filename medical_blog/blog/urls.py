from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsListView.as_view(), name='blog_url'),
    path('search_result/', SearchResultView.as_view(), name='search_result'),
    path('create/', CreateFormView.as_view(), name='create'),
    path('tags/', TagsListView.as_view(), name='tags_list_url'),

    path('tag/<str:tag_slug>/update/', TagUpdate.as_view(), name='update_tag_url'),
    path('post/<str:post_slug>/update/', PostUpdate.as_view(), name='update_post_url'),

    path('post/<str:post_slug>/', PostBodyView.as_view(), name='post_body_url'),
    path('tag/<str:tag_slug>/', TagView.as_view(), name='tag_url'),

    path('<str:post_slug>/delete/', delete_post, name='post_delete_url'),
    path('<str:tag_slug>/delete_tag/', delete_tag, name='tag_delete_url'),
]

