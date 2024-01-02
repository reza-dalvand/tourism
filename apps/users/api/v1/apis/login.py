from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers import LoginSerializer


# If you need to customize login use this, else use TokenObtainPairView, TokenRefreshView
class LoginApi(APIView):
    """
    handel authorization with phone number and password

    Parameters:
        - phone: string
        - password: string

    Returns:
        - refresh token: String
        - access token: String
    """

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.validated_data["phone"]
            password = serializer.validated_data["password"]
            # Walrus Technic
            if user := authenticate(request=request, phone=phone_number, password=password):
                login(request, user)
                refresh = RefreshToken.for_user(user)
                tokens = {"refresh_token": str(refresh), "access_token": str(refresh.access_token)}
                return Response(data={"tokens": tokens}, status=status.HTTP_200_OK)
        return Response(data={"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
