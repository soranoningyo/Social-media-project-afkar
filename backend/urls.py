"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import routers
from .settings import dev
from .api.views import index_view,EssaysViewSet,TarhViewSet,LoginView,RegisterUserView,LogoutView,ProfileView,CommentViewSet
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register('essays', EssaysViewSet)
router.register('Tarh', TarhViewSet,"tot")
router.register('prox', ProfileView)
router.register(r'comment',CommentViewSet)

urlpatterns = [


    # http://localhost:8000/api/<router-viewsets>
    re_path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    re_path('api/admin/', admin.site.urls),
    url(r'^registers/$', RegisterUserView.as_view(), name='user-register'),
    url(r'^login/$', LoginView.as_view(), name='user-login'),
    url(r'^logout/$', LogoutView.as_view(), name='user-logout'),
    # url(r'^current/$', UserView.as_view(), name='user-current'),
    # http://localhost:8000/
    re_path(r'^.*$', index_view),
    
]

urlpatterns += static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)


