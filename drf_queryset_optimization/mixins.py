class QuerysetOptimizationMixin:

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.defer_fields:
            queryset = queryset.defer(*self.defer_fields)
        elif self.only_fields:
            queryset = queryset.only(*self.only_fields)

        return queryset
