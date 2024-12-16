from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path("maskapai/", views.maskapai, name="maskapai"),
    path("details/<int:ticket_id>", views.ticketDetails, name="ticketDetails"),
    path('flight/<int:ticket_id>/seat/<int:seat_id>/book/', views.book_seat, name='book_seat'),
    path("flight/<int:ticket_id>/ticket-info/<int:reservation_id>", views.displayTicket, name="ticket-info"),

    # include
    path("", include('Authenticated.urls')),
]