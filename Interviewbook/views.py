from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect,render,get_object_or_404
from django.utils import timezone
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'Interviewbook/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'Interviewbook/signup.html', {'form': form})

def login_view(request):
    _message = 'Log in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'Interviewbook/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')


def ListResponses(request):
    responses = InterviewResponse.objects.filter(timestamp__lte=timezone.now()).order_by('-timestamp')
    paginator = Paginator(responses, 10) # Show 10 responses per page
    page = request.GET.get('page')
    responses = paginator.get_page(page)
    return render(request, 'Interviewbook/responses.html', {'responses': responses})

def ListResponsesbyCompany(request):
    query=request.GET['company']
    company= get_object_or_404(Company, name=query)
    responses = InterviewResponse.objects.filter(company= company.id).order_by('-hits')
    paginator = Paginator(responses, 10) # Show 10 responses per page
    page = request.GET.get('page')
    responses = paginator.get_page(page)
    return render(request, 'Interviewbook/responses.html', {'responses': responses})


def viewResponse(request, response_id):
    response = get_object_or_404(InterviewResponse, id=response_id)
    response.increase()
    return render(request, 'Interviewbook/response.html', {'response': response})


def updateResponse(request, response_id):
    instance = get_object_or_404(InterviewResponse, id=response_id)
    form = ResponseForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'Interviewbook/Responseform.html', {'form': form})

def deleteResponse(request,response_id):
    instance = get_object_or_404(InterviewResponse, id=response_id).delete()
    return redirect('ListResponses')

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
