from django.urls import path,register_converter
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('photo/article', views.new_article, name='new-post'),
    path('photo/profile', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)