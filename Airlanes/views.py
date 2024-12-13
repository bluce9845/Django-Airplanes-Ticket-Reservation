from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Maskapai, Seats, TicketReservation
from .forms import ReservationForm

def home(request):
    if request.method == "POST":
        searched1 = request.POST['searched-1']
        searched2 = request.POST['searched-2']
        searched3 = request.POST['searched-3']

        searched = Maskapai.objects.filter(lokasiPertama__icontains=searched1, lokasiTujuan__icontains=searched2, tgl_takeoff__icontains=searched3)
   

        context = {
            'searched1': searched1,
            'searched2': searched2,
            'searched3': searched3,
            'searched' : searched,
        }
        
        if not searched1 and searched2 and searched3:
            messages.success(request, "That days not cant fly try for more days...")
            return render(request, 'home.html', context)
        else:
            request.session['searched1'] = searched1
            request.session['searched2'] = searched2
            request.session['searched3'] = searched3
            return render(request, 'maskapai/search.html', context)
    else:
        return render(request, 'home.html',{})

def maskapai(request):
    maskapai = Maskapai.objects.all()

    context = {
        'maskapai' : maskapai,
    }
    return render(request, 'maskapai.html', context)


def ticketDetails(request, ticket_id):
    try:
        maskapai = Maskapai.objects.get(id=ticket_id)
        seats = maskapai.seats.all() 
    except Maskapai.DoesNotExist:
        return HttpResponse("Maskapai tidak ditemukan", status=404)

    form_input = ReservationForm
    selected_seat = None

    if request.method == "POST":
        seat_id = request.POST.get('seat_id')
        seat_number = request.POST.get('seat_number')

        if seat_id:
            try:
                selected_seat = maskapai.seats.get(id=seat_id)
                # Proses penyimpanan data ke model TicketReservation
                ticket_reservation = TicketReservation(
                    seat=selected_seat,
                    namaLengkap=request.POST.get('namaLengkap'),
                    nik=request.POST.get('nik'),
                    waktuPembelian=request.POST.get('waktuPembelian'),

                )
                ticket_reservation.save()
                
                # Tandai seat sebagai sudah dipesan
                selected_seat.is_booked = True
                selected_seat.save()

                messages.success(request, "Seat berhasil dipesan.")
                return HttpResponseRedirect(reverse('ticketDetails', args=[ticket_id]))
            except maskapai.seats.model.DoesNotExist:
                return HttpResponse("Seat tidak ditemukan", status=404)

    context = {
        'maskapai': maskapai,
        'seats': seats,
        'selected_seat': selected_seat,
        'form': form_input,
    }
    return render(request, 'ticket/details.html', context)


def book_seat(request, ticket_id, seat_id):
    if request.method == "POST":
        seat = get_object_or_404(Seats, id=seat_id, flight_id=ticket_id)

        if not seat.is_booked:

            
            seat.is_booked = True
            seat.save()

            return HttpResponseRedirect(reverse('ticketDetails', args=[ticket_id]))
        else:
            messages.error(request, "Seat already booked.")
            return HttpResponseRedirect(reverse('ticketDetails', args=[ticket_id]))