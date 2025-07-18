from django.shortcuts import render,redirect
from .models import Events
from django.db.models  import Q
from apps.cameramen.models import Cameramen
from django.contrib.auth.decorators import login_required

# Create your views here.
# add event
@login_required
def add_event(request):
  cameramens = Cameramen.objects.filter(user_id = request.user.id)

  if request.method == 'POST':
    userid = request.user.id
    eventName = request.POST.get('eventName')
    eventDescription = request.POST.get('eventDescription')
    eventDate = request.POST.get('date')
    eventLocation = request.POST.get('location')
    price = request.POST.get('price')
    
    selected_ids = request.POST.getlist('cameramens')
    event = Events.objects.create(
      user_id = userid,  
      event_name = eventName,
      event_description = eventDescription,
      event_date = eventDate,
      location = eventLocation,
      price = price,
    )
    event.cameramen.set(selected_ids)
    event.save()
    return redirect('all_event')
  return render(request,'event_temp/add_event.html',{'cameramens':cameramens})




# all Events
@login_required
def all_events(request):
  events = Events.objects.filter(user_id=request.user.id)
  query = request.GET.get('q','')

  if query:
    events = Events.objects.filter(Q(event_name__icontains=query) | Q(event_date__icontains=query) | Q(location__icontains=query) )

  return render(request,'event_temp/all_events.html',{'events':events})


def edit_event(request, id):
  event = Events.objects.filter(id=id).first()

  if request.method == 'POST':
    eventName = request.POST.get('eventName')
    eventDescription = request.POST.get('eventDescription')
    eventDate = request.POST.get('date')
    eventLocation = request.POST.get('location')
    price = request.POST.get('price')

    event.event_name = eventName
    event.event_description = eventDescription
    event.location = eventLocation
    event.price = price
    if eventDate:
      event.event_date = eventDate
    event.save()
    return redirect('all_event')

  return render(request,'event_temp/edit_event.html',{"event":event})


def delete_event(request,id):
  event = Events.objects.filter(id=id).first()
  event.delete()
  return redirect('all_event')