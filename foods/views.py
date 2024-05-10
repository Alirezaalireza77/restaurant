from django.shortcuts import render
from .models import Food


def food_list(request):
    """this functions used to get an list of all food from our model
    and display them to a html page that is list.html"""
    food_list = Food.objects.all()
    context = {
        'foods': food_list
    }
    return render(request, 'foods/index.html', context)


def food_detail(request, id):
    """this function used to get an special(object)food from our food list"""
    food = Food.objects.get(id=id)
    context ={
        "food": food
    }
    return render(request, 'foods/detail.html', context)