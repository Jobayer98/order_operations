from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def index(request):
    return Response({"msg": "Hello world"})

urlpatterns = [
    path('', index, name='home'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
