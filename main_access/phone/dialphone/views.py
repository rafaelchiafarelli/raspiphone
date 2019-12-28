from django.shortcuts import render

# Create your views here.
def dial(request):
    return render(request, 'dialphone/dial.html',{})