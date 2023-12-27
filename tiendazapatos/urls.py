from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    # Agregamos urls del sitio de autenticacion de django
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    # URLs para el manejo de la autenticación.
    path('accounts/ login/ [name="login"]', include('django.contrib.auth.urls')),
    path('accounts/ logout/ [name="logout"]', include('django.contrib.auth.urls')),
    path('accounts/ password_change/ [name="password_change"]', include('django.contrib.auth.urls')),
    path('accounts/ password_change/done/ [name="password_change_done"]', include('django.contrib.auth.urls')),
    path('accounts/ password_reset/ [name="password_reset"]', include('django.contrib.auth.urls')),
    path('accounts/ password_reset/done/ [name="password_reset_done"]', include('django.contrib.auth.urls')),
    path('accounts/ reset/<uidb64>/<token>/ [name="password_reset_confirm"]', include('django.contrib.auth.urls')),
    path('accounts/ reset/done/ [name="password_reset_complete"]', include('django.contrib.auth.urls')),
]
# Se configuran las carpetas de las imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)