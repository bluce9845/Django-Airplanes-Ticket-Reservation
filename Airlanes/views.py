from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Maskapai, Seats, TicketReservation
from .forms import ReservationForm, SearchTickets

def home(request):
    searchForm = SearchTickets()
    
    if request.method == "POST":
        form = SearchTickets(request.POST)
        if form.is_valid():   
            searched1 = form.cleaned_data['lokasiPertama']
            searched2 = form.cleaned_data['lokasiTujuan']
            searched3 = form.cleaned_data['tglBerangkat']
            searched4 = form.cleaned_data['pilihClass']
    
            # Debug
            # print(f"Name : {searched1}")

            searched = Maskapai.objects.filter(lokasiPertama__icontains=searched1, lokasiTujuan__icontains=searched2, tgl_takeoff__icontains=searched3, clas__icontains=searched4)
   

            context = {
                'searched1': searched1,
                'searched2': searched2,
                'searched3': searched3,
                'searched4': searched4,
                'searched' : searched,
            }
        
            if not searched1 and searched2 and searched3 and searched4:
                messages.success(request, "That days not cant fly try for more days...")
                return render(request, 'home.html', context)
            else:
                request.session['searched1'] = searched1
                request.session['searched2'] = searched2
                request.session['searched3'] = searched3
                request.session['searched4'] = searched4
                return render(request, 'maskapai/search.html', context)
        else:
            form = SearchTickets()
    else:
        form = {
            'form': searchForm
        }

        # request.session.clear()

        return render(request, 'home.html', form)

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
        namaLengkap = request.POST.get('namaLengkap')
        nik = request.POST.get('nik')
        waktuPembelian = request.POST.get('waktuPembelian')
        seat_number = request.POST.get('seat_number')

        if seat_id:
            try:
                selected_seat = maskapai.seats.get(id=seat_id)

                request.session['ticket_data'] = {
                    'seat_id': seat_id,
                    'namaLengkap': namaLengkap,
                    'nik': nik,
                    'waktuPembelian': waktuPembelian,
                }

                # print(f"Ticket data : {request.POST['ticket_data']}")
                
                # Proses penyimpanan data ke model TicketReservation
                ticket_reservation = TicketReservation(
                    seat=selected_seat,
                    namaLengkap=request.POST.get('namaLengkap'),
                    nik=request.POST.get('nik'),
                    waktuPembelian=request.POST.get('waktuPembelian')
                )
                
                ticket_reservation.save()

                # Tandai seat sebagai sudah dipesan
                selected_seat.is_booked = True
                selected_seat.save()

                messages.success(request, "Seat berhasil dipesan.")
                return HttpResponseRedirect(reverse('ticket-info', args=[ticket_id]))
            except maskapai.seats.model.DoesNotExist:
                return HttpResponse("Seat tidak ditemukan", status=404)


    keys_to_remove = ['searched1', 'searched2', 'searched3', 'searched4']
    
    for key in keys_to_remove:
        if key in request.session:
            del request.session[key]

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

            return HttpResponseRedirect(reverse('ticket-info', args=[ticket_id]))
        else:
            messages.error(request, "Seat already booked.")
            return HttpResponseRedirect(reverse('ticketDetails', args=[ticket_id]))



def displayTicket(request, ticket_id):
    data_ticket = Maskapai.objects.get(id=ticket_id)
    data = data_ticket.seats.all()
    ticket_data = request.session.get('ticket_data')

    if not ticket_data:
        print("Session items:", request.session.items())
        return HttpResponse("Data tidak ditemukan di session", status=404)

    # Ambil detail spesifik
    seat_id = ticket_data.get('seat_id')
    namaLengkap = ticket_data.get('namaLengkap')
    nik = ticket_data.get('nik')
    waktuPembelian = ticket_data.get('waktuPembelian')

    context = {
        'data': data_ticket,
        'seat_id': seat_id,
        'namaLengkap': namaLengkap,
        'nik': nik,
        'waktuPembelian': waktuPembelian,
    }
    
    return render(request, 'ticket/displayInfoTicket.html', context)