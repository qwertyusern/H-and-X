from django.shortcuts import render
from .models import *
def result(request):
    qidirish=request.GET.get("searched")
    t=Togri.objects.filter(soz=qidirish)
    if len(t)==1:
        n=Notogri.objects.filter(togri=t[0])
    else:
        n = Notogri.objects.filter(xato_soz=qidirish)
        if len(n) == 1:
            t = Togri.objects.filter(id=n[0].togri.id)
            n = Notogri.objects.filter(togri=t[0])
    return render(request, "result.html", {"togri":t.first(), "notogri":n})




