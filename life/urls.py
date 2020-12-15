from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('tasks/', include('tasks.urls')),
    path('dairy/', include('dairy.urls')),
    url(r'^markitup/', include('markitup.urls')),
    url('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns = [
                    path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
