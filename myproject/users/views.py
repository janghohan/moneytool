from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def detail(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404("없는 아이디")

    return render(request,'users/detail.html', {'customer': customer})