from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from gins.models import Distillery, Gin


def all_distilleries(request):
    """ A view to show all distilleries, including sorting and search queries """

    distilleries = Distillery.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                distilleries = distilleries.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            distilleries = distilleries.order_by(sortkey)

# Have commented this out for now as the search form is in base.html and already deals with queries from
#gins but I somehow need that search function to include distilleries
#and I don't think I should be duplicating all this here unless I chaneg it to 'search gins'
#on th other page and 'search distilleries ' here. TO FOLLOW UP
    # if request.GET:
    #     if 'q' in request.GET:
    #         query = request.GET['q']
    #         if not query:
    #             messages.error(request, "You didn't enter any search criteria!")
    #             return redirect(reverse('distilleries'))
            
    #         queries = Q(name__icontains=query) | Q(description__icontains=query)
    #         distilleries = distilleries.filter(queries)


    current_sorting = f'{sort}_{direction}'

    context = {
        'distilleries': distilleries,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'distilleries/distilleries.html', context)


def individual_distillery(request, distillery_id):
    """ A view to show individual distillery details """

    distillery = get_object_or_404(Distillery, pk=distillery_id)

    context = {
        'distillery': distillery,
    }

    return render(request, 'distilleries/individual_distillery.html', context)