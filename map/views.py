from datetime import datetime
from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return render(request, 'helloworld.html', {
        'current_time': datetime.now(),
    })
