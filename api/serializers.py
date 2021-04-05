from rest_framework import serializers
from .models import BatchRecords


class BatchRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchRecords
        fields = '__all__'
