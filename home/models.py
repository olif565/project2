from django.db import models


class Data(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    # ppm_ch4 = models.CharField("ppm CH4", max_length=50, blank=True, null=True)
    # ppm_c2h4 = models.CharField("ppm C2H4", max_length=50, blank=True, null=True)
    # ppm_c2h2 = models.CharField("ppm C2H2", max_length=50, blank=True, null=True)
    persen_ch4 = models.CharField("%CH4", max_length=50, blank=True, null=True)
    persen_c2h4 = models.CharField("%C2H4", max_length=50, blank=True, null=True)
    persen_c2h2 = models.CharField("%C2H2", max_length=50, blank=True, null=True)
    fault = models.CharField("Fault", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no
