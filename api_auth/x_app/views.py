# import necessary modules
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail
# from django.utils.encoding import force_bytes, force_str
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


from .serializers import (RegisterSerializer)
                        #   PasswordResetRequestSerializer, PasswordResetConfirmSerializer)


@api_view(["POST"])
def register(request):
    """
    API endpoint for user registration
    """
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(APIView):
    """
    API endpoint for user authentication
    """

    def post(self, request):
        """
        API endpoint for user authentication
        """
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class CustomTokenRefreshView(APIView):
    """
    API endpoint for token refresh
    """

    def post(self, request):
        """
        API endpoint for token refresh
        """
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response(
                {"error": "No refresh token provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            refresh = RefreshToken(refresh_token)
            access = str(refresh.access_token)
            return Response({"access": access})
        except TokenError:
            return Response(
                {"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED
            )

# @api_view(["POST"])
# def password_reset_request(request):
#     serializer = PasswordResetRequestSerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data["email"]
#         user = User.objects.get(email=email)
#         token = default_token_generator.make_token(user)
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         current_site = get_current_site(request)
#         reset_link = (
#             f"http://{current_site.domain}/password-reset-confirm/{uid}/{token}/"
#         )

#         # Send email
#         send_mail(
#             "Password Reset Request",
#             f"Please use the following link to reset your password: {reset_link}",
#             "webmaster@example.com",
#             [email],
#             fail_silently=False,
#         )
#         return Response(
#             {"message": "Password reset email sent."}, status=status.HTTP_200_OK
#         )
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# def password_reset_confirm(request):
#     serializer = PasswordResetConfirmSerializer(data=request.data)
#     if serializer.is_valid():
#         uid = force_str(urlsafe_base64_decode(serializer.validated_data["uidb64"]))
#         user = User.objects.get(pk=uid)
#         token = serializer.validated_data["token"]
#         new_password = serializer.validated_data["new_password"]

#         if default_token_generator.check_token(user, token):
#             user.set_password(new_password)
#             user.save()
#             return Response(
#                 {"message": "Password has been reset successfully."},
#                 status=status.HTTP_200_OK,
#             )
#         return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
