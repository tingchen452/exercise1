import csv
import os
from api.models import BatchRecords


def run():
    file = open(
        'C:/Users/Ting/Desktop/python2/exercise1/scripts/example_batch_records.csv')  # Change this to the .csv file path and change '\' to '/'
    read_file = csv.reader(file)

    BatchRecords.objects.all().delete()

    for batch in read_file:
        print(batch)
        BatchRecords.objects.create(
            batch_number=batch[0], submitted_at=batch[1] if batch[1] else None, nodes_used=batch[2] if batch[2]else None)
