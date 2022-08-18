from django_filters import CharFilter, FilterSet, NumberFilter
from reviews.models import Title


class TitleFilter(FilterSet):
    """Класс для фильтрации произведений."""

    name = CharFilter(field_name='name', lookup_expr='contains')
    genre = CharFilter(field_name='genre__slug')
    category = CharFilter(field_name='category__slug')
    year = NumberFilter(field_name='year')

    class Meta:
        model = Title
        fields = ('genre', 'category', 'name', 'year')
