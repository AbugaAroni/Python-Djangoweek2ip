from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome, name='Welcome'),
    re_path('search/', views.search_results, name='search_results'),
    re_path('singleimage/(\d+)',views.singleimage,name ='View image'),
    path('accounts/profile/', views.profile, name='user_profile'),
    re_path('viewuser/(\d+)', views.view_user, name='view_userprofile'),    
    path('new/post', views.new_post, name='new_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
