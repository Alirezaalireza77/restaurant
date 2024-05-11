from django.shortcuts import render


def reserve(request):
    """to display the reservation page"""
    context = {}
    return render(request, 'reservation/reservation.html', context)



