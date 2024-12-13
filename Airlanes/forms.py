from django.forms import ModelForm
from django import forms
from .models import TicketReservation

class ReservationForm(forms.Form):
    namaLengkap = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'name':'namaLengkap','placeholder':'Nama Lengkap'}))
    nik = forms.CharField(label="", max_length=16,widget=forms.TextInput(attrs={'class':'form-control', 'name':'nik','placeholder':'Nik'}))
    waktuPembelian = forms.CharField(label="Waktu Pembelian", widget=forms.TimeInput(attrs={'type':'time', 'class':'form-control', 'name':'waktuPembelian','placeholder':'Waktu Pembelian'}))
    # waktuPembelian = forms.TimeField(label="", widget=forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Waktu Pembelian'}))
    
    class Meta:
        model = TicketReservation
        fields = ('namaLengkap', 'nik', 'waktuPembelian', 'seat')