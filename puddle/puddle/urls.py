
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from core.views import contact, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('contact/', contact, name='contact'),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
