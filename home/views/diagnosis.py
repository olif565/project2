import numpy as np

from home.models import Diagnosis


def get_diagnosis():

    data = []

    databenar = 0

    db = Diagnosis.objects.all()
    for x in db:
        if x.f1 is not None:
            f1 = float(x.f1)
            fk1 = int(np.sign(f1))
        else:
            f1 = '-'
            fk1 = '-'

        if x.f2 is not None:
            f2 = float(x.f2)
            fk2 = int(np.sign(f2))
        else:
            f2 = '-'
            fk2 = '-'

        if x.f3 is not None:
            f3 = float(x.f3)
            fk3 = int(np.sign(f3))
        else:
            f3 = '-'
            fk3 = '-'

        if x.f4 is not None:
            f4 = float(x.f4)
            fk4 = int(np.sign(f4))
        else:
            f4 = '-'
            fk4 = '-'

        if x.f5 is not None:
            f5 = float(x.f5)
            fk5 = int(np.sign(f5))
        else:
            f5 = '-'
            fk5 = '-'

        if x.f6 is not None:
            f6 = float(x.f6)
            fk6 = int(np.sign(f6))
        else:
            f6 = '-'
            fk6 = '-'

        if x.f7 is not None:
            f7 = float(x.f7)
            fk7 = int(np.sign(f7))
        else:
            f7 = '-'
            fk7 = '-'

        d = {
            'no': x.no,
            'f1': f1,
            'fk1': fk1,
            'f2': f2,
            'fk2': fk2,
            'f3': f3,
            'fk3': fk3,
            'f4': f4,
            'fk4': fk4,
            'f5': f5,
            'fk5': fk5,
            'f6': f6,
            'fk6': fk6,
            'f7': f7,
            'fk7': fk7,
            'hasil': x.hasil,
            'aktual': x.aktual
        }
        data.append(d)

        if x.akurasi == '1':
            databenar = databenar + 1

    akurasi = (databenar / len(db)) * 100

    diagnosis = {
        'data': data,
        'akurasi': akurasi,
    }

    return diagnosis
