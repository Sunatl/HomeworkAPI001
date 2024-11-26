from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .serialaizes import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class VakanListAPIVIEW(ListAPIView):
    queryset = Vakansi.objects.all().order_by("-id")
    serializer_class = Vakansiserial
    permissions_classes = [IsAuthenticated]

    def get(self, request):
        context = {"message": "Hello, World!"} 
        return Response(context)

class VakanCreateAPIVIEW(CreateAPIView):
    serializer_class = Vakansiserial

class VakanRetrieveAPIView(RetrieveAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = Vakansiserial

class VakanRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = Vakansiserial

class VakanDestroyAPIView(DestroyAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = Vakansiserial

class VakanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = Vakansiserial

# Worker Views
class WorkerListAPIVIEW(ListAPIView):
    queryset = Worker.objects.all().order_by("-id")
    serializer_class = WorkerSerial
    permission_classes = [IsAuthenticated]

class WorkerCreateAPIVIEW(CreateAPIView):
    serializer_class = WorkerSerial

class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerial

class WorkerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerial

class WorkerDestroyAPIView(DestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerial

class WorkerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerial