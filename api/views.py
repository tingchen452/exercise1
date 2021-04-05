from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BatchRecordsSerializer
from .models import BatchRecords

# Create your views here.


@api_view(['GET'])
def BatchApiView(request):
    batches = BatchRecords.objects.all()
    submitted_after = request.query_params.get('submitted_after')
    submitted_before = request.query_params.get('submitted_before')
    min_nodes = request.query_params.get('min_nodes')
    max_nodes = request.query_params.get('max_nodes')

    if min_nodes:
        batches = batches.filter(nodes_used__gte=min_nodes)
    if max_nodes:
        batches = batches.filter(nodes_used__lte=max_nodes)
    if submitted_before:
        batches = batches.filter(submitted_at__lte=submitted_before)
    if submitted_after:
        batches = batches.filter(submitted_at__gte=submitted_after)

    # serializer = BatchRecordsSerializer(batches, many=True)

    batch_records = []

    for index, tmp in enumerate(batches, start=1):
        batchid = index
        batchNum = tmp.batch_number
        submittedAt = tmp.submitted_at
        nodesUsed = tmp.nodes_used

        record = {
            "type": "batch_jobs",
            "id": batchid,
            "attributes":
            {
                "batch_number": batchNum,
                "submitted_at": submittedAt,
                "nodes_used": nodesUsed
            }
        }
        batch_records.append(record)

    return Response(
        {
            "links": {
                "self": request.build_absolute_uri()
            },
            'data': batch_records
        }

    )
