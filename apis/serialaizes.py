from rest_framework.serializers import ModelSerializer
from .models import *

class Vakansiserial(ModelSerializer):
    class Meta:
        model = Vakansi
        fields = "__all__"
        
class WorkerSerial(ModelSerializer):
    class Meta:
        model =  Worker
        fields = "__all__"
