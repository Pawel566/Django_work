from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room

def book_room(request):
    return render(request, 'book_room.html')

def add_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector_availability = request.POST.get('projector_availability') == 'on'

        if not room_name:
            return HttpResponse("Nazwa sali nie może być pusta.", status=400)
        if Room.objects.filter(name=room_name).exists():
            return HttpResponse("Sala o tej nazwie już istnieje.", status=400)
        if int(capacity) <= 0:
            return HttpResponse("Pojemność sali musi być liczbą dodatnią.", status=400)

        Room.objects.create(name=room_name, capacity=capacity, projector_availability=projector_availability)
        return redirect('home')
    else:
        return render(request, 'add_room.html')

from django.shortcuts import render
from .models import Room

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})