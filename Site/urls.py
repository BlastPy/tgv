

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$', 'wiki.views.index'),
    url(r'^rozdil/(?P<is_main>\w+)', 'wiki.views.stats'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
