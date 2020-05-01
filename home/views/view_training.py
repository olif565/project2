from django.views.generic import ListView
from home.views import training
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_training.html'
    context_object_name = 'data'

    def get_queryset(self, **kwargs):

        level = self.kwargs['level']

        matriks = training.get_matriks(level)
        n_data_normalisasi = matriks['n_data_normalisasi']
        n_list_data_matriks = matriks['n_list_data_matriks']
        n_list_data_matriks_view = matriks['n_list_data_matriks_view']

        data_error_rate = training.get_error_rate(n_list_data_matriks)['data_error_rate']
        data_delta_alfa = training.get_delta_alfa(data_error_rate)['data_delta_alfa']
        data_alfa_baru = training.get_alfa_baru(data_delta_alfa)['data_alfa_baru']

        context = {
            'level': level,
            'n_data_normalisasi': n_data_normalisasi,
            'n_list_data_matriks_view': n_list_data_matriks_view,
            'data_error_rate': data_error_rate,
            'data_delta_alfa': data_delta_alfa,
            'data_alfa_baru' : data_alfa_baru
        }

        return context
