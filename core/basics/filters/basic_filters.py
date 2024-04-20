import django_filters
from django.db import models
from django_filters import CharFilter


class BasicFilter(django_filters.FilterSet):
    search = django_filters.CharFilter()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        model = kwargs.get('queryset').model
        for filter_ in self.filters.values():
            if type(filter_) is CharFilter:
                filter_.lookup_expr = 'icontains'
            filter_.model = model
            filter_.parent = self

    def filter_queryset(self, queryset):
        searchs = self.request.GET
        new_queryset = queryset.none()
        for name, value in self.form.cleaned_data.items():
            if name is 'search':
                continue
            for name_search, search_term in searchs.items():
                if search_term:
                    try:
                        new_queryset = self.filters[name].filter(queryset, search_term) | new_queryset
                    except:
                        pass
            assert isinstance(
                queryset, models.QuerySet
            ), "Expected '%s.%s' to return a QuerySet, but got a %s instead." % (
                type(self).__name__,
                name,
                type(queryset).__name__,
            )
        return new_queryset
