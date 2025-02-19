
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BotStatusView(APIView):
    def get(self, request):
        # Логика для проверки статуса бота
        return Response({"status": "Bot is running"}, status=status.HTTP_200_OK)
