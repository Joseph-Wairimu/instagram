from django.urls import path,register_converter
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('photo/article', views.new_article, name='new-post'),
    path('photo/profile', views.profile, name='profile'),
    path('photo/new_profile', views.update_profile, name='new_profile'),
    path('search/', views.search_results, name='search_results'),
    path('comment/<int:id>', views.comment, name='comment'),
    path('like/', views.like_post, name='like-post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)