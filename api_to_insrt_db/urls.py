from django.urls import path
from .views import upload_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/upload/', upload_file, name='upload_excel'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print("URL patterns:")
for url in urlpatterns:
    print(url.name)