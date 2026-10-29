from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import ReservationForm
def home(request): return render(request,'index.html')
@require_POST
def reserve(request):
    form=ReservationForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'message':' '.join(f'{field}: {" ".join(errors)}' for field,errors in form.errors.items())},status=400)
    booking=form.save()
    return JsonResponse({'message':f'Request #{booking.pk} saved. Your table is pending restaurant confirmation.'},status=201)
