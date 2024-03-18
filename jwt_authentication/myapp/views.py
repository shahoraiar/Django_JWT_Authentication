from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import MyModel
from .serializers import MyModelSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class RestrictedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     return Response(data={"message": "You have access to this restricted content."})
    def get(self, request):
        queryset = MyModel.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

    