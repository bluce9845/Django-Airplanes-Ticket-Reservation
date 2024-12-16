from django.forms import ModelForm
from django import forms
from .models import TicketReservation, Maskapai

class SearchTickets(forms.Form):
    OPTIONS = [
        ('economy', 'Economy'),
        ('economy_vip', 'Vip Economy'),
        ('busines', 'Business'),
        ('frist_class', 'Frist Class')
    ]
    
    lokasiPertama = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Dari', 'type':'text', 'class':'form-control', 'name':'searched-1', 'id':'searched-1'}))
    lokasiTujuan = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Ke', 'type':'text', 'class':'form-control', 'name':'searched-2', 'id':'searched-2'}))
    tglBerangkat = forms.CharField(label="Keberangkatan", widget=forms.TextInput(attrs={'type':'date', 'class':'form-control', 'name':'searched-3', 'id':'searched-3'}))
    pilihClass = forms.ChoiceField(choices=OPTIONS, label="Pilih Class", widget=forms.Select(attrs={'class':'form-label', 'name':'searched-4', 'id':'searched-4'}))

    class Meta:
        model: Maskapai
        fields = ('lokasiPertama', 'lokasiTujuan', 'tglBerangkat', 'pilihClass')

class ReservationForm(forms.Form):
    # Choice datas
    
    namaLengkap = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'name':'namaLengkap','placeholder':'Nama Lengkap'}))
    nik = forms.CharField(label="", max_length=16,widget=forms.TextInput(attrs={'class':'form-control', 'name':'nik','placeholder':'Nik'}))
    waktuPembelian = forms.CharField(label="Waktu Pembelian", widget=forms.TimeInput(attrs={'type':'time', 'class':'form-control', 'name':'waktuPembelian','placeholder':'Waktu Pembelian'}))
    # jumlahTicket = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'number', 'class':'form-control', 'name':'jumlahTicket', 'id':'jumlahTicket', 'placeholder':'Jumlah Ticket'}))
    
    class Meta:
        model = TicketReservation
        fields = ('namaLengkap', 'nik', 'waktuPembelian', 'seat')