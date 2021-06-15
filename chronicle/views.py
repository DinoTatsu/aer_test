from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import Event, Chronicle
from .serializers import EventSerializer, ChronicleSerializer, ChronicleWithDaysSerializer


class ChronicleWithDaysView(generics.RetrieveAPIView):
    serializer_class = ChronicleWithDaysSerializer
    queryset = Chronicle.objects.all()

    def get_object(self):
        unique_id = self.kwargs.get('unique_id')
        return Chronicle.objects.get(unique_id=unique_id)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response(status=404, data={'error': _('Объект не найден')})
        serializer = self.get_serializer(instance)
        return super(ChronicleWithDaysView, self).retrieve(request, *args, **kwargs)


class ChronicleList(viewsets.ModelViewSet):
    queryset = Chronicle.objects.all()
    serializer_class = ChronicleSerializer


class EventList(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
