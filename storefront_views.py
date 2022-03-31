from django.views import generic

from .models import PopularCollection


class PopularCollectionsList(generic.ListView):
    model = PopularCollection
    template_name = 'popular_collections/list.html'
