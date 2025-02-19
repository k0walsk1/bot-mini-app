
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/status/', BotStatusView.as_view(), name='bot_status'),
]
