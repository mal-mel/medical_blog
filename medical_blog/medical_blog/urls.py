from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import MainPageView, update_news_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view()),
    path('blog/', include('blog.urls')),
    path('news/', include('news.urls')),
    path('update_news_list/', update_news_list)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
