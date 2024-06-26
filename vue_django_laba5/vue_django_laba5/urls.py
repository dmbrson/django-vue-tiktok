from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.views import FrontendTemplateView, RegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', FrontendTemplateView.as_view(), name='index'),
    path('api/register/', RegisterView.as_view(), name='register')
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)