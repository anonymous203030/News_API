# import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="News API",
      default_version='v1',
      description="News API Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="aram.simonyan.03@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
a = 'api/v1/'
urlpatterns = [
        #ADMIN
    path('admin/', admin.site.urls),
        #APPS URLS ENDPOINTS
    path(f'{a}posts/', include('posts.urls')),
    path(f'{a}users/', include('users.urls')),
    path(f'{a}comments/', include('comments.urls')),
    path(f'{a}subscription/', include('subscription.urls')),

    #SWAGGER

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('paypal/', include('paypal.standard.ipn.urls') )
    #   DJANGO-DEBUG-TOOLBAR
     ]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),

] + urlpatterns