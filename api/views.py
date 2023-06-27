from rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.models import  User
from api.serializer import CustomRegisterSerializer, GetUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = GetUserSerializer


class GetUserData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(pk=self.request.user.id)
            serializer = GetUserSerializer(user, many=False)
            return Response(
                {"detail": serializer.data},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
