from django import forms
from . models import Reservation

class ReservationForm(forms.ModelForm):
    """reservatiion form to reserve table"""
    class Meta:
        model = Reservation
        # get all of fields object of Reservation model from the user
        fields = "__all__"
