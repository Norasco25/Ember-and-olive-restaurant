from django import forms
from django.utils import timezone
from .models import Reservation
class ReservationForm(forms.ModelForm):
    time=forms.ChoiceField(choices=[(x,x) for x in ['17:00','18:00','19:00','20:00','21:00']])
    guests=forms.IntegerField(min_value=1,max_value=8)
    class Meta:
        model=Reservation
        fields=['name','email','date','time','guests']
    def clean_date(self):
        date=self.cleaned_data['date']
        if date<timezone.localdate(): raise forms.ValidationError('Choose today or a future date.')
        if date.weekday()==0: raise forms.ValidationError('We are closed on Mondays.')
        return date
