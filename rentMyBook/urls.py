
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include("accounts.urls")), 
    path('accounts/', include("django.contrib.auth.urls")),   # working for login.html
]

