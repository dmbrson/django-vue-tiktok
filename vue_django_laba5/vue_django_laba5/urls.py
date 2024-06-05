from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.views import FrontendTemplateView

urlpatterns = [
    path('', FrontendTemplateView.as_view(), name='index')
]
urlpatterns += staticfiles_urlpatterns()