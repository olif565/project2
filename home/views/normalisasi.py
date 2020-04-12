from home.models import Data


def get_normalisasi():

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
            'fault': x.fault,
            'kelas': 1
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

    for i, x in enumerate(n_data_normalisasi):
        if x['fault'] == 'D1':
            x['fault'] = '1'
        else:
            x['fault'] = '2'

    for i, x in enumerate(n_data_normalisasi):
        if x['fault'] == '1':
            x['kelas'] = '1'
        else:
            x['kelas'] = '-1'

    # End Normalisasi

    data_normalisasi = {
        'n_data_normalisasi': n_data_normalisasi
    }

    return data_normalisasi
