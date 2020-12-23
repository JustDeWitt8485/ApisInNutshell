# from django.shortcuts import render


from api.models import Manufacturer, Shoe, ShoeColor, ShoeType
from api.serializers import ManufacturerSerializer, ShoeSerializer, ShoeColorSerializer, ShoeTypeSerializer


from rest_framework import viewsets


# Create your views here.,
'''
Class

ShoeTypeViewSet

queryset ShoeType.obj.all()

serializer
'''

"""

Fun fact about Joe's life
growing up on the
African Savanna: He used to hunt with the maasai worriers


"""


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
