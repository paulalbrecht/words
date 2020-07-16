from django.http import JsonResponse
from django.db.models import Count

from .models import Recommendation

def by_count(request, count=1):
    qs = list(Recommendation.objects.all().values('title', 'author').annotate(recommendations=Count('recommender')).filter(recommendations=count))
    response = JsonResponse(qs, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    return response
