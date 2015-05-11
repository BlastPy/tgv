

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$', 'wiki.views.all_parts'),
    url(r'^test/$', 'wiki.views.test_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
