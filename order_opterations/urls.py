from django.contrib import admin
from django.urls import path, include
from api.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
