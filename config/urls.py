from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from product.views import toggle_like
from product.views import *
from django.conf.urls.static import static
from django.conf import settings

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title='Fullstack_hakaton',
        default_version='v1',
        description='My API'
    ),
    public=True
)
router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/myaccount/', include('myaccount.urls')),
    path('api/v1/products/<int:id>/toggle_like/', toggle_like),
    path('api/v1/export/', include('product.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


