from datetime import datetime
from django.shortcuts import render
from map.models import station, info

# Create your views here.
def helloworld(request):
    return render(request, 'helloworld.html', {
        'current_time':datetime.now(),
    })

def chart(request, pk):
    obj = station.objects.get(pk=pk)
    name = obj.sno;
    aall = info.objects.filter(sno__exact=name)
    a = []
    b = []
    for i in aall:
        a[len(a):] = [i.mday.strftime("%m/%d/%Y")]
        b[len(b):] = [i.bemp]
    return render(request,'index.html',{'labels':a, 'data':b, 'stop_name':obj.sna})

def home(request):
    obj = station.objects.all()
    return render(request,'helloworld.html',{'obj':obj})

"""
def chart(request):
    obj = info.objects.filter(sno__exact='0001')
    a = []
    b = []
    for i in obj:
        a[len(a):] = [i.mday.strftime("%m/%d/%Y")]
        b[len(b):] = [i.bemp]

    return render(request, 'index.html', {
        'obj': obj,
        'labels': a,
        'data': b,
    })
"""
