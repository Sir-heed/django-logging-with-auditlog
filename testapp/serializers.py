import json
from auditlog.models import LogEntry
from rest_framework import serializers

from .models import Choice, Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

    def to_representation(self, instance):
        """Using the object history field to get all its history"""
        data = super().to_representation(instance)
        history = instance.history.all()
        data['history'] = LogEntrySerializer(history, many=True).data
        return data


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'

    def to_representation(self, instance):
        """changes are stored as json text, hence need to load it"""
        data = super().to_representation(instance)
        data['changes'] =json.loads(data['changes'])
        return data
