from django.db import models

class Maskapai(models.Model):
    lokasiPertama = models.CharField(max_length=200, null=True)
    lokasiTujuan = models.CharField(max_length=200, null=True)
    tgl_takeoff = models.DateField(null=True)
    nameMaskapai = models.CharField(max_length=200)
    hargaTicket = models.CharField(max_length=200)
    bandaraPertama = models.CharField(max_length=200, null=True)
    bandaraTujuan = models.CharField(max_length=200, null=True)
    jamBerangkat = models.TimeField(null=True)
    jamSampai = models.TimeField(null=True)
    clas = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.nameMaskapai} ({self.lokasiPertama} -> {self.lokasiTujuan}) ({self.bandaraPertama} -> {self.bandaraTujuan})"


class Seats(models.Model):
    flight = models.ForeignKey(Maskapai, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seat_number} ({'Booked' if self.is_booked else 'Available'})"

class TicketReservation(models.Model):
    seat = models.ForeignKey('Seats', on_delete=models.CASCADE)
    namaLengkap = models.CharField(max_length=200)
    nik = models.CharField(max_length=16)
    waktuPembelian = models.TimeField()

    def __str__(self):
        return f"{self.namaLengkap} {self.nik}"