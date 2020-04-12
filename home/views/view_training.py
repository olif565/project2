from django.views.generic import ListView
from home.views import training
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_training.html'
    context_object_name = 'data'

    def get_queryset(self):
        n_data_normalisasi = training.get_training()['n_data_normalisasi']
        n_list_data_training_view = training.get_training()['n_list_data_training_view']

        context = {
            'n_data_normalisasi': n_data_normalisasi,
            'n_list_data_training_view': n_list_data_training_view
        }

        return context
