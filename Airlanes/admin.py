from django.contrib import admin
from .models import Maskapai, Seats, TicketReservation

@admin.register(Maskapai)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('nameMaskapai', 'tgl_takeoff')
    actions = ['generate_seats']

    def generate_seats(self, request, queryset):
        for flight in queryset:
            rows = 10  # Jumlah baris kursi
            cols = 6   # Jumlah kolom kursi
            seat_letters = "ABCDEF"[:cols]
            seats = []

            for row in range(1, rows + 1):
                for letter in seat_letters:
                    seat_number = f"{row}{letter}"  # Format nomor kursi (contoh: "1A", "10F")
                    seats.append(Seats(flight=flight, seat_number=seat_number))

            Seats.objects.bulk_create(seats)  # Menambahkan banyak kursi sekaligus
            self.message_user(request, f"Generated {len(seats)} seats for flight {flight.nameMaskapai}")
    generate_seats.short_description = "Generate seats for selected flights"

admin.site.register(TicketReservation)
admin.site.register(Seats)
