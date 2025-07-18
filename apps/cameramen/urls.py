from django.urls import path
from . import views



urlpatterns = [
  path('add-new-cameramen/',views.add_cameramen, name='add_cameramen'),
  path('all-cameramen/',views.cameramen_list, name='all_cameramens'),
  path('edit-cameramen/<int:id>',views.edit_cameramen, name='edit_cameramen'),
  path('all-cameramen/<int:id>',views.delete_cameramen, name='delete_cameramen'),


  
]
