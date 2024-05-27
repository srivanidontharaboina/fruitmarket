from django.shortcuts import get_object_or_404, render

from Market.models import Fruit

# Create your views here.
def fruit_detail(request,pk):
    fruit=get_object_or_404(Fruit,pk=pk)
    context={
        'fruit':fruit,
    }
    return render(request,'fruit_detail.html',context)