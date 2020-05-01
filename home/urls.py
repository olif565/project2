"""ProjectSkripsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from home.views import view_data, view_normalisasi, view_training

app_name = 'home'

urlpatterns = [
    path('', view_data.dashboard, name='index'),
    path('list', view_data.IndexView.as_view(), name='list'),
    path('<int:pk>/', view_data.DataDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', view_data.edit, name='edit'),
    path('create/', view_data.create, name='create'),
    path('delete/<int:pk>/', view_data.delete, name='delete'),

    path('normalisasi/<int:level>/', view_normalisasi.IndexView.as_view(), name='normalisasi'),
    path('training/<int:level>/', view_training.IndexView.as_view(), name='training'),
]
