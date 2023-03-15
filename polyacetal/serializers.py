from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import home_poly, ffmm_page, bcm_page, bes_page, el_page, ma_page


class poly_serializer(ModelSerializer):
    class Meta:
        model = home_poly
        fields = ['id', 'poly_index_001', 'poly_index_002', 'poly_index_003',
                  'poly_index_004', 'poly_index_005', 'poly_index_006']


class ffmm_serializer(ModelSerializer):
    class Meta:
        model = ffmm_page
        fields = ['id', 'ffmm_tit', 'ffmm_num', 'ffmm_img', 'ffmm_det']
