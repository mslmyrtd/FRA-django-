
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
class RegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        seriliazer=RegisterSerializer(data=request.data)
        seriliazer.is_valid(raise_exception=True)
        seriliazer.save()
        return Response(
            {"message":"user created succesfully"}
        )
