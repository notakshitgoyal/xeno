from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lead.models import Lead
# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
