from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import AddLeadForm
from .models import Lead
from django.contrib import messages
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)
    return render(request, 'lead/leads_list.html', {'leads': leads})

@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, 'lead/leads_details.html', {'lead': lead})

@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()
    messages.success(request, 'Lead deleted successfully')
    return redirect('leads_list')


@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lead updated successfully!')
            return redirect('leads_list')
    else:
        form = AddLeadForm(instance=lead) 
    return render(request, 'lead/edit_lead.html', {'form': form})

@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, 'Lead added successfully!')
            return redirect('leads_list')
    else:
        form = AddLeadForm()
    return render(request, 'lead/add_lead.html', {'form': form})