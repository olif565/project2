import logging

from django.shortcuts import render
from django.views.generic import ListView

from home.forms import NormalisasiForm
from home.models import Training
from home.views import kernel
from home.views import normalisasi

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_normalisasi.html'
    context_object_name = 'data'

    def get_queryset(self, **kwargs):

        try:
            data = Training.objects.get(id='1')
            if data is None:
                form = NormalisasiForm()
                sigma = None
            else:
                form = NormalisasiForm(initial={'sigma': data.sigma})
                sigma = data.sigma
        except Training.DoesNotExist:
            form = NormalisasiForm()
            sigma = None

        level = self.kwargs['level']

        n_data_normalisasi = []
        n_list_data_kernel_view = []

        if level == 1:
            display_form = 'block'
            display_result = 'none'
        else:
            display_form = 'none'

            if sigma is not None:
                display_result = 'block'
                n_data_normalisasi = normalisasi.get_normalisasi(level)['n_data_normalisasi']
                n_list_data_kernel_view = kernel.get_kernel(n_data_normalisasi, float(sigma))['n_list_data_kernel_view']

                # Save to DB
                normalisasi.save_normalisasi_to_db()
            else:
                display_result = 'none'

        context = {
            'level': level,
            'n_data_normalisasi': n_data_normalisasi,
            'n_list_data_kernel_view': n_list_data_kernel_view,
            'display_form': display_form,
            'display_result': display_result,
            'form': form
        }

        return context

    # Handle POST HTTP requests
    def post(self, request, *args, **kwargs):
        form = NormalisasiForm(request.POST)

        level = self.kwargs['level']

        if form.is_valid():
            sigma = form.cleaned_data['sigma']

            try:
                param = Training.objects.get(id='1')
            except Training.DoesNotExist:
                param = Training()
                param.id = '1'

            param.sigma = sigma
            param.save()

            n_data_normalisasi = normalisasi.get_normalisasi(level)['n_data_normalisasi']
            n_list_data_kernel_view = kernel.get_kernel(n_data_normalisasi, float(sigma))['n_list_data_kernel_view']

            # Save to DB
            normalisasi.save_normalisasi_to_db()

            context = {
                'level': level,
                'n_data_normalisasi': n_data_normalisasi,
                'n_list_data_kernel_view': n_list_data_kernel_view,
                'display_form': 'block',
                'display_result': 'block',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})
        else:
            context = {
                'level': level,
                'n_data_normalisasi': [],
                'n_list_data_kernel_view': [],
                'display': 'none',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})

