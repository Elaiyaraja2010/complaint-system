from django.shortcuts import render, redirect
from .models import Complaint

def raise_complaint(request):
    if request.method == 'POST':
        Complaint.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            description=request.POST['description']
        )
        return redirect('/')

    return render(request, 'raise_complaint.html')
def check_status(request):
    complaints = []
    searched = False

    if request.method == 'POST':
        searched = True
        email = request.POST.get('email')
        complaints = Complaint.objects.filter(email=email)

    return render(request, 'check_status.html', {
        'complaints': complaints,
        'searched': searched
    })

