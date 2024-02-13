from django.shortcuts import render
from .models import Vendor

# Create your views here.
def index(request):
    return render(request, 'vendor/index.html', {
        'vendor': Vendor.objects.all()
    })
