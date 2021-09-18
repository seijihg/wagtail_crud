from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReviewSerializer
from rest_framework import viewsets

from .models import Review

# class ReviewViewSet(APIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     def get(self, request, format=None):
#         queryset = Review.objects.all()
#         serializer_class = ReviewSerializer(queryset, many=True)
#         return Response(serializer_class.data)


class ReviewqMixin(object):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewViewSet(ReviewqMixin, viewsets.ModelViewSet):
    pass
