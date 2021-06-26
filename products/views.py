from django.shortcuts import render
from .models import Items


def list_view(request):
    context = {
        'items':Items.objects.all()
    }

#    context["dataset"]= Items.objects.all()

    return render(request, 'base.html', context)
