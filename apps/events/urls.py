from django.urls import path
from . import views



urlpatterns = [
  path('add-new-event/',views.add_event, name='add_event'),
  path('all-event/',views.all_events, name='all_event'),
  path('edit-event/<int:id>/',views.edit_event, name='edit_event'),
  path('all-event/<int:id>/',views.delete_event, name='delete_event'),


  
]
