from home.models import Data
from django.views.generic import ListView
import math
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'home_normalisasi.html'
    context_object_name = 'data'

    def get_queryset(self):
        listdata = Data.objects.all()
        list_persen_ch4 = Data.objects.values_list('persen_ch4', flat=True)
        list_persen_c2h4 = Data.objects.values_list('persen_c2h4', flat=True)
        list_persen_c2h2 = Data.objects.values_list('persen_c2h2', flat=True)

        minvalue = {
            'persen_ch4': min([float(i) for i in list_persen_ch4]),
            'persen_c2h4': min([float(i) for i in list_persen_c2h4]),
            'persen_c2h2': min([float(i) for i in list_persen_c2h2])
        }

        maxvalue = {
            'persen_ch4': max([float(i) for i in list_persen_ch4]),
            'persen_c2h4': max([float(i) for i in list_persen_c2h4]),
            'persen_c2h2': max([float(i) for i in list_persen_c2h2])
        }

        n_data_normalisasi = []
        n_list_data_kernel = []
        n_persen_ch4 = []
        n_persen_c2h4 = []
        n_persen_c2h2 = []

        # Normalisasi
        for x in listdata:
            data = {
                'no': x.no,
                'persen_ch4': 0,
                'persen_c2h4': 0,
                'persen_c2h2': 0,
                'fault': x.fault
            }
            n_data_normalisasi.append(data)

        for i, x in enumerate(list_persen_ch4):
            n = (float(x) - minvalue['persen_ch4']) / (maxvalue['persen_ch4'] - minvalue['persen_ch4'])
            n_persen_ch4.append(n)
            n_data_normalisasi[i]['persen_ch4'] = float(n)

        for i, x in enumerate(list_persen_c2h4):
            n = (float(x) - minvalue['persen_c2h4']) / (maxvalue['persen_c2h4'] - minvalue['persen_c2h4'])
            n_persen_c2h4.append(n)
            n_data_normalisasi[i]['persen_c2h4'] = float(n)

        for i, x in enumerate(list_persen_c2h2):
            n = (float(x) - minvalue['persen_c2h2']) / (maxvalue['persen_c2h2'] - minvalue['persen_c2h2'])
            n_persen_c2h2.append(n)
            n_data_normalisasi[i]['persen_c2h2'] = float(n)

        # End Normalisasi


        # Kernel

        s = 2

        for i, x in enumerate(n_data_normalisasi):
            n_data_kernel = []

            for j, y in enumerate(n_data_normalisasi):
                n1 = math.pow((x['persen_ch4'] - y['persen_ch4']), 2)
                n2 = math.pow((x['persen_c2h4'] - y['persen_c2h4']), 2)
                n3 = math.pow((x['persen_c2h2'] - y['persen_c2h2']), 2)

                k = math.exp((-(n1+n2+n3)) / (2 * (math.pow(s, 2))))

                if  j == 0:
                    n_data_kernel.append(x['no'])

                n_data_kernel.append(k)

            n_list_data_kernel.append(n_data_kernel)

        # End Kernel

        context = {
            'n_data_normalisasi': n_data_normalisasi,
            'n_list_data_kernel': n_list_data_kernel
        }

        return context