from rest_framework import serializers

from .models import Event, Chronicle


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class ChronicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chronicle
        fields = '__all__'


class ChronicleWithDaysSerializer(serializers.ModelSerializer):
    requires_context = True
    chronicle_events = serializers.SerializerMethodField()

    class Meta:
        model = Chronicle
        fields = (
            'min_timestamp',
            'max_timestamp',
            'aircraft',
            'status',
            'unique_id',
            'chronicle_events',
        )

    def get_chronicle_events(self, obj):
        try:
            n = getattr(self.context['request'], 'parser_context')['kwargs']['n']
            if n:
                return obj.n_days_of_chronicle(n)
        except Exception as err:
            return obj.n_days_of_chronicle()
