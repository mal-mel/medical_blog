from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view()),
    path('blog/', include('blog.urls')),
    path('news/', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
