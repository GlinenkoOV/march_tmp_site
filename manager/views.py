from django.shortcuts import render, redirect
from main_app.models import Reservation
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/') #Перевіряємо щоб залогінений був користувач
@user_passes_test(is_manager)        #Перевіряємо щоб  користувач належав до групи менеджер
def reservation_list(request):
    messages = Reservation.objects.filter(is_processed=False)
    return render(request, 'reservation_list.html', context={'reservations': messages})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request,pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations')
