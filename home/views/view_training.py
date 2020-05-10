from django.shortcuts import render
from django.views.generic import ListView

from home.forms import TrainingForm
from home.views import training
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_training.html'
    context_object_name = 'data'

    def get_queryset(self, **kwargs):

        form = TrainingForm()

        level = self.kwargs['level']

        context = {
            'level': level,
            'n_data_normalisasi': [],
            'n_list_data_matriks_view': [],
            'data_iterasi': [],
            'display': 'none',
            'form': form
        }

        return context

    # Handle POST HTTP requests
    def post(self, request, *args, **kwargs):
        form = TrainingForm(request.POST)

        level = self.kwargs['level']

        if form.is_valid():
            lamda = float(form.cleaned_data['lamda'])
            # sigma = form.cleaned_data['sigma']
            constant = float(form.cleaned_data['constant'])
            gamma = float(form.cleaned_data['gamma'])
            iterasi = int(form.cleaned_data['iterasi'])

            matriks = training.get_matriks(level, lamda)
            n_data_normalisasi = matriks['n_data_normalisasi']
            n_list_data_matriks = matriks['n_list_data_matriks']
            n_list_data_matriks_view = matriks['n_list_data_matriks_view']

            data_iterasi = training.get_iterasi(n_list_data_matriks, constant, gamma, iterasi)

            context = {
                'level': level,
                'n_data_normalisasi': n_data_normalisasi,
                'n_list_data_matriks_view': n_list_data_matriks_view,
                'data_iterasi': data_iterasi,
                'display': 'block',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})
        else:
            context = {
                'level': level,
                'n_data_normalisasi': [],
                'n_list_data_matriks_view': [],
                'data_iterasi': [],
                'display': 'none',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})
