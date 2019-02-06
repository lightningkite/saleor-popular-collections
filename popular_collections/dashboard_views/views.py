from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from saleor.core.utils import get_paginator_items
from saleor.dashboard.views import staff_member_required
from .filters import PopularCollectionFilter
from .forms import PopularCollectionForm

from ..models import PopularCollection


@staff_member_required
@permission_required('popular_collections.view')
def popular_collection_list(request):
    popular_collections = (
        PopularCollection.objects.all().select_related('collection')
        .order_by('collection'))
    popular_collection_filter = PopularCollectionFilter(
        request.GET, queryset=popular_collections)
    popular_collections = get_paginator_items(
        popular_collection_filter.qs, settings.DASHBOARD_PAGINATE_BY, request.GET.get('page'))
    # Call this so that cleaned_data exists on the filter_set
    popular_collection_filter.form.is_valid()
    ctx = {
        'popular_collections': popular_collections, 'filter_set': popular_collection_filter,
        'is_empty': not popular_collection_filter.queryset.exists()}
    return TemplateResponse(request, 'popular_collections/dashboard/list.html', ctx)


@staff_member_required
@permission_required('popular_collections.edit')
def popular_collection_create(request):
    popular_collection = PopularCollection()
    form = PopularCollectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Dashboard message', 'Created popular collection')
        messages.success(request, msg)
        return redirect('popular-collection-dashboard-list')
    ctx = {'popular_collection': popular_collection, 'form': form}
    return TemplateResponse(request, 'popular_collections/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('popular_collections.edit')
def popular_collection_details(request, pk):
    popular_collection = PopularCollection.objects.get(pk=pk)
    form = PopularCollectionForm(
        request.POST or None, instance=popular_collection)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated popular collection %s') % popular_collection.name
        messages.success(request, msg)
        return redirect('popular-collection-dashboard-list')
    ctx = {'popular_collection': popular_collection, 'form': form}
    return TemplateResponse(request, 'popular_collections/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('popular_collections.edit')
def popular_collection_delete(request, pk):
    popular_collection = get_object_or_404(PopularCollection, pk=pk)
    if request.method == 'POST':
        popular_collection.delete()
        msg = pgettext_lazy('Dashboard message',
                            'Removed popular collection %s') % popular_collection
        messages.success(request, msg)
        return redirect('popular-collection-dashboard-list')
    return TemplateResponse(
        request, 'popular_collections/dashboard/modal/confirm_delete.html', {'popular_collection': popular_collection})
