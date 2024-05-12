from django.shortcuts import render
from .forms import ReservationForm

def reserve(request):
    """to display the reservation page"""
    reserve_form = ReservationForm()
    if request.method == "POST":
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReservationForm()
    context = {
        'form': reserve_form,
    }
    return render(request, 'reservation/reservation.html', context)




