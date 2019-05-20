from django.urls import path
from .views import NewsView

urlpatterns = [
    path('<str:title>/', NewsView.as_view(), name='news_page_url'),
]
