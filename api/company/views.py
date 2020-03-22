from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets


from company.models import *
from company.serializers import *


class CompanyFilter(filters.FilterSet):
    min_total_assets = filters.NumberFilter(field_name='total_assets', lookup_expr='gte')
    max_total_assets = filters.NumberFilter(field_name='total_assets', lookup_expr='lte')

    class Meta:
        model = Company
        fields = ['name', 'series_name', 'min_total_assets', 'max_total_assets']


class CompanyViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter
