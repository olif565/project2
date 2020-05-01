from django.views.generic import ListView
from home.views import normalisasi
from home.views import kernel
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_normalisasi.html'
    context_object_name = 'data'

    def get_queryset(self, **kwargs):

        level = self.kwargs['level']

        n_data_normalisasi = normalisasi.get_normalisasi(level)['n_data_normalisasi']
        n_list_data_kernel_view = kernel.get_kernel(level)['n_list_data_kernel_view']

        context = {
            'level': level,
            'n_data_normalisasi': n_data_normalisasi,
            'n_list_data_kernel_view': n_list_data_kernel_view
        }

        return context
