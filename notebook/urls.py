from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('port-mngrvision/', admin.site.urls),
    path('', include('portfolio.urls', namespace="portfolio")),
]
