import math

from home.models import DataTesting, HasilTraining, Training


def proses_training():

    data_testing = get_data_testing()
    data_training = get_data_training()
    sigma = get_sigma()

    for i, x in enumerate(data_testing):

        data_alpha = []

        for j, y in enumerate(data_training):

            n1 = math.pow((x['persen_ch4'] - y['n_ch4']), 2)
            n2 = math.pow((x['persen_c2h4'] - y['n_c2h4']), 2)
            n3 = math.pow((x['persen_c2h2'] - y['n_c2h2']), 2)

            k = math.exp((-(n1 + n2 + n3)) / (2 * (math.pow(sigma, 2))))

            a = float(y['alpha']) * float(y['kelas']) * k

            data_alpha.append(a)




def get_data_testing():

    listdata = DataTesting.objects.all()
    list_persen_ch4 = DataTesting.objects.values_list('persen_ch4', flat=True)
    list_persen_c2h4 = DataTesting.objects.values_list('persen_c2h4', flat=True)
    list_persen_c2h2 = DataTesting.objects.values_list('persen_c2h2', flat=True)

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

    for x in listdata:
        data = {
            'no': x.no,
            'persen_ch4': 0,
            'persen_c2h4': 0,
            'persen_c2h2': 0
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

    return n_data_normalisasi


def get_data_training():

    db = HasilTraining.objects.all()
    data_training = []

    for x in db:
        data = {
            'no': x.no,
            'level': x.level,
            'n_ch4': x.n_ch4,
            'n_c2h4': x.n_c2h4,
            'n_c2h2': x.n_c2h2,
            'fault': x.fault,
            'kelas': x.kelas,
            'alpha': x.alpha
        }
        data_training.append(data)

    return data_training


def get_sigma():
    db = Training.objects.all()

    sigma = 2
    if len(db) > 0:
        sigma = db[0].sigma

    return sigma
