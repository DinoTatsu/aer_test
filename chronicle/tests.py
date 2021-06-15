from django.test import TestCase


from chronicle.models import Chronicle
from chronicle.serializers import ChronicleWithDaysSerializer
c = Chronicle.objects.first()
print(ChronicleWithDaysSerializer(c).data)
