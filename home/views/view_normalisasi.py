import logging

from django.shortcuts import render
from django.views.generic import ListView

from home.models import Training
from home.views import normalisasi

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_normalisasi.html'
    context_object_name = 'data'

    def get_queryset(self, **kwargs):
        
        data = Training.objects.get(id='1')

        level = self.kwargs['level']

        n_data_normalisasi = []
        
        display_result = 'block'
        n_data_normalisasi = normalisasi.get_normalisasi(level)['n_data_normalisasi']

        context = {
            'level': level,
            'n_data_normalisasi': n_data_normalisasi,
            'display_result': display_result,
        }

        return context