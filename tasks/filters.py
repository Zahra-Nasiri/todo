from django_filters import DateFilter, FilterSet

from tasks.models import Task


class TaskFilter(FilterSet):
    due_date__gt = DateFilter(field_name='due_date', lookup_expr='gt')
    due_date__gte = DateFilter(field_name='due_date', lookup_expr='gte')
    due_date__lt = DateFilter(field_name='due_date', lookup_expr='lt')
    due_date__lte = DateFilter(field_name='due_date', lookup_expr='lte')

    created_at__gt = DateFilter(field_name='created_at', lookup_expr='gt')
    created_at__gte = DateFilter(field_name='created_at', lookup_expr='gte')
    created_at__lt = DateFilter(field_name='created_at', lookup_expr='lt')
    created_at__lte = DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['due_date', 'created_at']
