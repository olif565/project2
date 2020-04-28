from django.views.generic import ListView
from home.views import training
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_training.html'
    context_object_name = 'data'

    def get_queryset(self):
        n_data_normalisasi = training.get_matriks()['n_data_normalisasi']
        n_list_data_matriks = training.get_matriks()['n_list_data_matriks']
        n_list_data_matriks_view = training.get_matriks()['n_list_data_matriks_view']
        data_error_rate = training.get_error_rate(n_list_data_matriks)['data_error_rate']
        data_delta_alfa = training.get_delta_alfa(data_error_rate)['data_delta_alfa']

        context = {
            'n_data_normalisasi': n_data_normalisasi,
            'n_list_data_matriks_view': n_list_data_matriks_view,
            'data_error_rate': data_error_rate,
            'data_delta_alfa': data_delta_alfa
        }

        return context
