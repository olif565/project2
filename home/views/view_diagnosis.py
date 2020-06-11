from django.views.generic import ListView

from home.views import diagnosis


class IndexView(ListView):
    template_name = 'home_diagnosis.html'
    context_object_name = 'data_list'

    def get_queryset(self):

        data_diagnosis = diagnosis.get_diagnosis()
        data = data_diagnosis['data']
        akurasi = data_diagnosis['akurasi']

        context = {
            'data': data,
            'akurasi': akurasi
        }

        return context
