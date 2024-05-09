from django.shortcuts import render
from .models import Food


def food_list(request):
    food_list = Food.objects.all()
    context = {
        'foods': food_list
    }
    return render(request, 'foods/list.html', context)
