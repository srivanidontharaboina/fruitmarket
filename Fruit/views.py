
from django.shortcuts import render

from Market.models import Fruit


def home(request):
    fruits=Fruit.objects.all()
    context={
        'fruits':fruits,
    }
    return render(request,'home.html',context)