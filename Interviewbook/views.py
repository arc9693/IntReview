from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect,render,get_object_or_404
from django.utils import timezone
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    return render(request, 'Interviewbook/index.html')

def ListResponses(request):
    responses = InterviewResponse.objects.filter(timestamp__lte=timezone.now()).order_by('timestamp')
    paginator = Paginator(responses, 10) # Show 10 responses per page
    page = request.GET.get('page')
    responses = paginator.get_page(page)
    return render(request, 'Interviewbook/responses.html', {'responses': responses})

def ListResponsesbyCompany(request):
    query=request.GET['company']
    company= get_object_or_404(Company, name=query)
    responses = InterviewResponse.objects.filter(company= company.id).order_by('hits')
    paginator = Paginator(responses, 10) # Show 10 responses per page
    page = request.GET.get('page')
    responses = paginator.get_page(page)
    return render(request, 'Interviewbook/responses.html', {'responses': responses})


def viewResponse(request, response_id):
    response = get_object_or_404(InterviewResponse, id=response_id)
    response.increase()
    return render(request, 'Interviewbook/response.html', {'response': response})

def response_new(request):
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.hits=0
            form.timestamp = timezone.now()
            form.save()
            return redirect('index')
    else:
        form = ResponseForm()
    return render(request, 'Interviewbook/Responseform.html', {'form': form})

def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('response_new')
    else:
        form = CompanyForm()
    return render(request, 'Interviewbook/CompanyForm.html', {'form': form})
