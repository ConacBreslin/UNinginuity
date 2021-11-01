from django.shortcuts import render, get_object_or_404
from gins.models import Distillery, Gin


def all_distilleries(request):
    """ A view to show all distilleries, including sorting and search queries """

    distilleries = Distillery.objects.all()

    context = {
        'distilleries': distilleries,
    }

    return render(request, 'distilleries/distilleries.html', context)


def individual_distillery(request, distillery_id):
    """ A view to show individual distillery details """

    distillery = get_object_or_404(Distillery, pk=distillery_id)

    context = {
        'distillery': distillery,
    }

    return render(request, 'distilleries/individual_distillery.html', context)