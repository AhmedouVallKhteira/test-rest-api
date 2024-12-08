from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='author')

router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('library/', include(router.urls)),  # تضمين الروابط الخاصة بتطبيق `library`
]
