from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Salom
from .serializers import SalomSerializer


class SalomApiView(ListCreateAPIView):
    queryset = Salom.objects.all()
    serializer_class = SalomSerializer


class SalomDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Salom.objects.all()
    serializer_class = SalomSerializer