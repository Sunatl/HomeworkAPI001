from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from .serialaizes import *
from .models import *

class VakanListAPIVIEW(ListAPIView):
    queryset =Vakansi.objects.all().order_by("-id")
    serializer_class = Vakansiserial
    
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
    serializer_class = Vakansi.objects.all()
    
class VakanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vakansi.objects.all()
    serializer_class = Vakansiserial
    
    

# Worker
class WorkerListAPIVIEW(ListAPIView):
    queryset = Worker.objects.all().order_by("-id")
    serializer_class = WorkerSerial
    
class WorkerCreateAPIVIEW(CreateAPIView):
    serializer_class = WorkerSerial
    
    
class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset =  Worker.objects.all()
    serializer_class = WorkerSerial
    
    
class WorkerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =  Worker.objects.all()
    serializer_class = WorkerSerial
    
    
class WorkerDestroyAPIView(DestroyAPIView):
    queryset =  Worker.objects.all()
    serializer_class =  Worker.objects.all()
    
class WorkerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerial