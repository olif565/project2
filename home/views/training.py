import math

from home.models import Training
from home.views import kernel
import logging

logger = logging.getLogger(__name__)


def get_matriks(level, lamda, sigma):

    s = sigma

    datakernel = kernel.get_kernel(level, s)
    n_data_normalisasi = datakernel['n_data_normalisasi']
    n_list_data_kernel = datakernel['n_list_data_kernel']
    n_list_data_kernel_view = datakernel['n_list_data_kernel_view']

    n_list_data_matriks = []
    n_list_data_matriks_view = []

    # lambda
    l = lamda

    for i, x in enumerate(n_list_data_kernel):
        n_data_matriks = []
        n_data_matriks_view = []
        y_i = int(n_data_normalisasi[i]['kelas'])

        for j, y in enumerate(x):
            y = float(n_list_data_kernel[i][j])
            y_j = int(n_data_normalisasi[j]['kelas'])

            # matrik
            d_ij = y_i * y_j * (y + (math.pow(l, 2)))

            if j == 0:
                # n_data_matriks_view.append(n_data_normalisasi[i]['no'])
                n_data_matriks_view.append(i+1)

            n_data_matriks_view.append(d_ij)
            n_data_matriks.append(d_ij)

        n_list_data_matriks.append(n_data_matriks)
        n_list_data_matriks_view.append(n_data_matriks_view)

    data_kernel = {
        'n_data_normalisasi': n_data_normalisasi,
        'n_list_data_matriks': n_list_data_matriks,
        'n_list_data_matriks_view': n_list_data_matriks_view
    }

    return data_kernel


def get_iterasi(list_data_matriks, constanta, gamma, i):

    data_iterasi = []

    alfa_baru = []

    for x in range(i):

        # alpha
        a = 0

        if x == 0:
            a = 0
        else:
            a = alfa_baru

        data_error_rate = get_error_rate(a, list_data_matriks)
        data_delta_alfa = get_delta_alfa(a, data_error_rate, constanta, gamma)
        data_alfa_baru = get_alfa_baru(a, data_delta_alfa)

        alfa_baru = data_alfa_baru

        iterasi = {
            'data_error_rate': data_error_rate,
            'data_delta_alfa': data_delta_alfa,
            'data_alfa_baru': data_alfa_baru
        }

        data_iterasi.append(iterasi)

    return data_iterasi


def get_error_rate(alpha, list_data_matriks):

    data_error_rate = []

    for i, x in enumerate(list_data_matriks):

        for j, y in enumerate(x):

            a = 0
            if alpha == 0:
                a = 0
            else:
                a = alpha[i]

            er = a * float(y)

            if i == 0:
                data_error_rate.append(er)
            else:
                data_error_rate[j] = data_error_rate[j] + er

    return data_error_rate


def get_delta_alfa(alpha, data_error_rate, constanta, gamma):

    # constant
    const = constanta

    # gamma
    g = gamma

    data_delta_alfa = []

    for i, x in enumerate(data_error_rate):

        a = 0
        if alpha == 0:
            a = 0
        else:
            a = alpha[i]

        da = min(max(g * (1 - x), -a), (const - a))
        data_delta_alfa.append(da)

    return data_delta_alfa

def get_alfa_baru(alpha, data_delta_alfa):

    data_alfa_baru = []

    for i, x in enumerate(data_delta_alfa):

        a = 0
        if alpha == 0:
            a = 0
        else:
            a = alpha[i]

        ab = a + x
        data_alfa_baru.append(ab)

    return data_alfa_baru
