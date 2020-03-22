from rest_framework import serializers
from company.models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'series_name', 'rep_pd_date', 'total_assets', 'total_liabilities', 'net_assets')
