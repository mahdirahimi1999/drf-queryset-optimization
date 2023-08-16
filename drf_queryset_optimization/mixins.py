class QuerysetOptimizationMixin:

    def get_queryset(self):
        queryset = super().get_queryset()

        defer_fields = getattr(self, 'defer_fields', [])
        only_fields = getattr(self, 'only_fields', [])

        if defer_fields:
            queryset = queryset.defer(*defer_fields)
        elif only_fields:
            queryset = queryset.only(*only_fields)

        return queryset
