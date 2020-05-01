import math
from home.views import kernel
import logging

logger = logging.getLogger(__name__)


def get_matriks(level):

    datakernel = kernel.get_kernel(level)
    n_data_normalisasi = datakernel['n_data_normalisasi']
    n_list_data_kernel = datakernel['n_list_data_kernel']
    n_list_data_kernel_view = datakernel['n_list_data_kernel_view']

    n_list_data_matriks = []
    n_list_data_matriks_view = []

    # lambda
    l = 0.5

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


def get_error_rate(list_data_matriks):

    # alpha
    a = 0

    data_error_rate = []

    for i, x in enumerate(list_data_matriks):

        for j, y in enumerate(x):

            er = a * float(y)

            if i == 0:
                data_error_rate.append(er)
            else:
                data_error_rate[j] = data_error_rate[j] + er

    error_rate = {
        'data_error_rate': data_error_rate
    }

    return error_rate


def get_delta_alfa(data_error_rate):

    # alpha
    a = 0

    # constant
    const = 1

    # gamma
    g = 0.01

    data_delta_alfa = []

    for i, x in enumerate(data_error_rate):

        da = min(max(g * (1 - x), -a), (const - a))
        data_delta_alfa.append(da)

    delta_alfa = {
        'data_delta_alfa': data_delta_alfa
    }

    return delta_alfa
