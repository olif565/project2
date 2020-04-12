import math
from home.views import kernel
import logging

logger = logging.getLogger(__name__)


def get_training():

    n_data_normalisasi = kernel.get_kernel()['n_data_normalisasi']
    n_list_data_kernel = kernel.get_kernel()['n_list_data_kernel']
    n_list_data_kernel_view = kernel.get_kernel()['n_list_data_kernel_view']

    n_list_data_training = []
    n_list_data_training_view = []

    # lambda
    l = 0.5

    for i, x in enumerate(n_list_data_kernel):
        n_data_training = []
        n_data_training_view = []
        y_i = int(n_data_normalisasi[i]['kelas'])

        for j, y in enumerate(x):
            y = float(n_list_data_kernel[i][j])
            y_j = int(n_data_normalisasi[j]['kelas'])

            # matrik
            d_ij = y_i * y_j * (y + (math.pow(l, 2)))

            if j == 0:
                n_data_training_view.append(n_data_normalisasi[i]['no'])

            n_data_training_view.append(d_ij)
            n_data_training.append(d_ij)

        n_list_data_training.append(n_data_training)
        n_list_data_training_view.append(n_data_training_view)

    data_kernel = {
        'n_data_normalisasi': n_data_normalisasi,
        'n_list_data_training_view': n_list_data_training_view
    }

    return data_kernel
