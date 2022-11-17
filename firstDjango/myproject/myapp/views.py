from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name' : 'Emre',
        'age' : 23,
        'nationality' : 'Turkish',
    }
    return render(request, 'firstwebpage.html', context)

def counter(request):
    text = request.POST['text']
    amountOfWords = len(text.split())
    return render(request, 'counter.html', {'amount' : amountOfWords}) 