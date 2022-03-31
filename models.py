from django.db import models

from django.utils.translation import pgettext_lazy

from saleor.core.permissions import MODELS_PERMISSIONS


# Add in the permissions specific to our models.
MODELS_PERMISSIONS += [
    'popular_collections.view',
    'popular_collections.edit'
]


class PopularCollection(models.Model):
    collection = models.OneToOneField(
        'product.Collection', on_delete=models.CASCADE, related_name='popular')
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'popular_collections'

        permissions = (
            ('view', pgettext_lazy('Permission description',
                                   'Can view popular collections')
             ),
            ('edit', pgettext_lazy('Permission description',
                                   'Can edit popular collections')))

    def __str__(self):
        return self.collection.name
