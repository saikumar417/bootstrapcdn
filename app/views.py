from django.shortcuts import render

# Create your views here.
def BS(request):
    return render(request, 'bootstrapcdn.html')