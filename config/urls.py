from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # juhoi.kim
    path('board/', include('board.urls')),
]
