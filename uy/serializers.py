from rest_framework.serializers import ModelSerializer
from .models import Salom


class SalomSerializer(ModelSerializer):

    class Meta:
        model = Salom
        fields = '__all__'
