from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogAG.views import Image, ImageDisplay


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('image/', Image.as_view(), name='image'),
    path('image/<int:pk>/', ImageDisplay.as_view(), name='image_display'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
