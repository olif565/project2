from django.shortcuts import render, redirect, get_object_or_404
from home.models import DataTesting
from home.forms import DataTestingForm
from django.views.generic import ListView, DetailView


def dashboard(request):
    return render(request, 'home.html', {})


class IndexView(ListView):
    template_name = 'home_data_testing.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataTesting.objects.all()


class DataDetailView(DetailView):
    model = DataTesting
    template_name = 'home_data_testing_detail.html'


def detail(request, pk, template_name='home_data_testing_detail.html'):
    data = get_object_or_404(DataTesting, pk=pk)
    return render(request, template_name, data)


def create(request):
    if request.method == 'POST':
        form = DataTestingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:data-testing')
    form = DataTestingForm()

    return render(request, 'home_data_testing_create.html', {'form': form})


def edit(request, pk, template_name='edit.html'):
    data = get_object_or_404(DataTesting, pk=pk)
    form = DataTestingForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('home:data-testing')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='confirm_delete.html'):
    contact = get_object_or_404(DataTesting, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home:data-testing')
    return render(request, template_name, {'object': contact})
