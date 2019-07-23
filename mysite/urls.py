from django.contrib import admin
from django.urls import path
from notifications.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', HomeView.as_view()),
]
