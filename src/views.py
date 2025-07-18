from django.shortcuts import render
from apps.customer.models import Customer
from apps.events.models import Events
import csv
from django.http import HttpResponse


def export_pending_customers_csv(request):
    customers = Customer.objects.all()
    pending_customers = [c for c in customers if c.pending_amount > 0]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pending_customers.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Mobile Number', 'Pending Amount'])

    for customer in pending_customers:
        writer.writerow([customer.full_name, customer.mobile_no, customer.pending_amount])

    return response




def dashboard(request):
    customers = Customer.objects.filter(user_id = request.user.id)
    events = Events.objects.filter(user_id = request.user.id)
    

    total_customers = customers.count()
    total_events = events.count()

    # Filter in Python since pending_amount is a property
    pending_customers = [customer for customer in customers if customer.pending_amount > 0]
    total_pending = sum(customer.pending_amount for customer in pending_customers)

    upcoming_events = events.order_by('event_date')[:5]


    context = {
        'total_customers': total_customers,
        'total_events': total_events,
        'pending_customers': pending_customers,
        'total_pending': total_pending,
        'upcoming_events': upcoming_events,
        'user': request.user,
    }
    return render(request, 'dashboard.html', context)
