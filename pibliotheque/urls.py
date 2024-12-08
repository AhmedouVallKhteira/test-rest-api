# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # للوصول إلى واجهة الـ Admin الخاصة بدجانغو
    path('api/', include('library.urls')),  # تضمين الروابط الخاصة بتطبيق `library`
]
