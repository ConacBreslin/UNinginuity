from django.shortcuts import render
from .models import Gin



def all_gins(request):
    """ A view to show all gins, including sorting and search queries """

    gins = Gin.objects.all()

    context = {
        'gins': gins,
    }

    return render(request, 'gins/gins.html', context)