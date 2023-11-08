import django_filters

from apps.item.models import Item


class ItemFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category__name',
        lookup_expr='icontains'
    )

    category_ids = django_filters.CharFilter(
        field_name='category__id',
        method='filter_category_ids'
    )

    def filter_category_ids(self, queryset, name, value):
        ids = [int(id) for id in value.split(',') if id.isdigit()]

        return queryset.filter(category__id__in=ids)

    @property
    def qs(self):
        qs = super().qs
        return qs.distinct()

    class Meta:
        model = Item
        fields = ['category', 'category_ids']

        # fields = ['name', 'city', 'price_min',
        #           'price_max', 'size', 'dimension', 'how_will_be_charged',
        #           'indicated_for_level', 'date_start', 'date_end'
        #           ]

        # price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
        # price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
        # size = django_filters.CharFilter(field_name='size', lookup_expr='icontains')
        # dimension = django_filters.CharFilter(field_name='dimension', lookup_expr='icontains')
        # how_will_be_charged = django_filters.CharFilter(field_name='how_will_be_charged', lookup_expr='icontains')
        # indicated_for_level = django_filters.CharFilter(field_name='indicated_for_level')
        # # gte maior ou igual
        # date_start = django_filters.DateFilter(field_name='date_start', lookup_expr='gte')
        # # lte menor ou igual
        # date_end = django_filters.DateFilter(field_name='date_end', lookup_expr='lte')
        # # data_range = django_filters.DateFromToRangeFilter(field_name='data')
