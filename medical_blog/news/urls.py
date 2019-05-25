from django.urls import path
from .views import NewsView, delete_news, UpdateNews

urlpatterns = [
    path('<str:slug>/delete/', delete_news, name='news_delete_url'),
    path('<str:slug>/update/', UpdateNews.as_view(), name='news_update_url'),
    path('<str:slug>/', NewsView.as_view(), name='news_page_url')
]
