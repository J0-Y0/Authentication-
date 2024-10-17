from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("", include("account_api.urls")),
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/doc",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger_documentation",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
if settings.DEBUG:
    urlpatterns += debug_toolbar_urls() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

admin.site.site_header = "e-Market | Administration"
admin.site.index_title = "Admin"
admin.site.site_title = "e-Market"
