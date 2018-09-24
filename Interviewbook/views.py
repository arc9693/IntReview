from django.http import HttpResponse
from .forms import ResponseForm
from django.shortcuts import redirect,render
from django.utils import timezone

def index(request):
    return HttpResponse("choose : 1.view response 2.submit response")

def ListResponses(request):
    return HttpResponse("1 2 3 4 5")

def viewResponse(request, response_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % response_id)

def response_new(request):
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.timestamp = timezone.now()
            form.save()
            return redirect('index')
    else:
        form = ResponseForm()
    return render(request, 'Interviewbook/Responseform.html', {'form': form})
