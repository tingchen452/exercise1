from django.db import models

# Create your models here.


class BatchRecords(models.Model):
    batch_number = models.IntegerField()
    submitted_at = models.DateTimeField(null=True, blank=True)
    nodes_used = models.IntegerField(null=True)
