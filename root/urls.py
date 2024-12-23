from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
from django.conf.urls.i18n import set_language

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('apps/', include('apps.urls')),
    path('management/', include('management.urls')),
    path('payment/', include('payment.urls')),

)
