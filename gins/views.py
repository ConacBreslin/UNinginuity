""" docstring"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Gin


def all_gins(request):
    """ A view to show all gins, including sorting and search queries """

    gins = Gin.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                gins = gins.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            gins = gins.order_by(sortkey)

            """I haven't used the category filtering used in Boutique ADO""" 

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('gins'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            gins = gins.filter(queries)

    context = {
        'gins': gins,
        'search_term': query,
    }

    return render(request, 'gins/gins.html', context)


def individual_gin(request, gin_id):
    """ A view to show individual gins """

    gin = get_object_or_404(Gin, pk=gin_id)

    context = {
        'gin': gin,
    }

    return render(request, 'gins/individual_gin.html', context)
