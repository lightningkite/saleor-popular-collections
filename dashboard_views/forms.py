from django import forms
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Collection
from ..models import PopularCollection


class PopularCollectionForm(forms.ModelForm):
    collection = forms.ModelChoiceField(
        queryset=Collection.objects.all())

    class Meta:
        model = PopularCollection
        verbose_name_plural = 'popular collections'
        fields = ['collection']

    def __init__(self, *args, **kwargs):
        super(PopularCollectionForm, self).__init__(*args, **kwargs)

        # Modify the queryset so that we don't show collections that are
        # already popular.
        # We need to do this differently for when the
        # user is adding vs editing so we can explicitly include the current
        # collection when they are editing.
        if self.instance.pk:
            self.fields['collection'].queryset = self.fields[
                'collection'].queryset.filter(
                    Q(id=self.instance.collection.pk) |
                    Q(popular__isnull=True))
        else:
            self.fields['collection'].queryset = self.fields[
                'collection'].queryset.filter(popular__isnull=True)
