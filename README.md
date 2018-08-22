# saleor-popular-collections

Popular Collections Plugin for [Saleor](https://github.com/mirumee/saleor)

This provides a (currently skeleton) implementation of popular/featured collections. This is currently built for the `v2018.6` tag of Saleor.

Adding the popular collections as a separate model allows for additional fields to be added specific to the popular/featured collection.

---

## Installation

To install, `pip install` the package as such:

```bash
pip install git+git://github.com/722c/saleor-popular-collections.git#egg='saleor-popular-collections'
```

Or list the package in your `requirements.txt` as such:

```
git+git://github.com/722c/saleor-popular-collections.git#egg='saleor-popular-collections'
```

Alternatively, this can be installed as a Git submodule directly in the root directory of your Saleor instance.

## Configuration

Once you have installed the app, you will need to add a few things to your project:

Add the app to your installed apps (the order doesn't matter):

```python
INSTALLED_APPS = [
    ...

    # Saleor plugins
    'saleor-popular-collections.popular_collections',

    ...
]
```

Add the apps URLs to your root `urls.py` in the `translatable_urlpatterns` near the bottom (this will allow any native Saleor URLs to be matched beforehand):

```python
translatable_urlpatterns = [
    ...
    url(r'^search/', include((search_urls, 'search'), namespace='search')),

    # URLs for saleor-popular-collections
    url(r'', include('saleor-popular-collections.popular_collections.urls')),

    url(r'', include('payments.urls'))
]
```

The frontend view lives at `/{language_code}/popular-collections`.

Finally, add the link to the dashboard by importing the template tag in `templates/dashboard/base.html` and putting it where you want in the side nav:

```django
<!DOCTYPE html>
{% load staticfiles i18n %}
 ...

 <!-- This is template tag you will need to load. -->
{% load popular_collections_side_nav from popular_collections %}

...

<ul class="side-nav">
  <li class="nav-home">
    <a href="{% url 'dashboard:index' %}">
      {% trans "Home" context "Dashboard homepage" %}
    </a>
  </li>
  {% if perms.product.view_product or perms.product.view_category %}
  <li class="side-nav-section" id="first">
    ...
  </li>
  {% endif %}

  <!-- Add in the saleor-popular-collections where you want. -->
  {% popular_collections_side_nav %}

  ...
</ul>

...
```
