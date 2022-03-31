from django.conf.urls import url

from . import storefront_views
from .dashboard_views import views as dashboard_views

urlpatterns = [
    url(r'^popular-collections/$',
        storefront_views.PopularCollectionsList.as_view(),
        name='popular-collection-list'),
    url(r'^dashboard/popular-collections/$',
        dashboard_views.popular_collection_list,
        name='popular-collection-dashboard-list'),
    url(r'^dashboard/popular-collections/create/$',
        dashboard_views.popular_collection_create,
        name='popular-collection-dashboard-create'),
    url(r'^dashboard/popular-collections/(?P<pk>[0-9]+)/$',
        dashboard_views.popular_collection_details,
        name='popular-collection-dashboard-detail'),
    url(r'^dashboard/popular-collections/(?P<pk>[0-9]+)/delete/$',
        dashboard_views.popular_collection_delete,
        name='popular-collection-dashboard-delete'),
]
