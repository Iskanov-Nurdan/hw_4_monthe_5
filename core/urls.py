from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


#drf_yasg
schema_view = get_schema_view(
   openapi.Info(
      title="17-1-B API",
      default_version='v1',
      description="17-1 description",
      terms_of_service="https://t.me/Ai_k_thoughts",
      contact=openapi.Contact(email="ainazikerkinbaeva2106200414@gmail.com",),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.task.urls')),  

#drf_yasg

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)