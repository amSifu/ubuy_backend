
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('ldsflldlld/', admin.site.urls),
    path('api/store/', include('store.urls')),
    path('api/users/', include('users.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
