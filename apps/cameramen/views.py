from django.shortcuts import render,redirect
from .models import Cameramen
from django.db.models import Q

# Create your views here.

def add_cameramen(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    mobile = request.POST.get('mobile')
    skills = request.POST.get('skills')

    Cameramen.objects.create(
    user_id = request.user.id,
    name = name,
    cameramen_mobile_no = mobile,
    skills = skills
  )
    return redirect('dashboard')
    

  return render(request,'cameramen/add_cameramen.html',)


# Cameramen list
def cameramen_list(request):
  cameramens = Cameramen.objects.filter(user_id=request.user.id)

  query = request.GET.get('q','')
  if query:
    cameramens = cameramens.filter(Q(name__icontains=query) | Q(cameramen_mobile_no__icontains=query) | Q(skills__icontains=query))
  return render(request,'cameramen/all_cameramens.html',{"cameramens":cameramens})


def edit_cameramen(request,id):
  cameramen = Cameramen.objects.filter(id=id).first()
  
  if request.method == 'POST':
    name = request.POST.get('name')
    mobileNo = request.POST.get('mobile')
    skills = request.POST.get('skills')

    cameramen.name = name
    cameramen.cameramen_mobile_no = mobileNo
    cameramen.skills = skills
    cameramen.save()
    return redirect('all_cameramens')
  
  return render(request,'cameramen/edit_cameramen.html',{'cameramen':cameramen})

def delete_cameramen(id):
 cameramen = Cameramen.objects.filter(id=id).first()
 cameramen.delete()
 return redirect('all_cameramens')