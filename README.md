drf-queryset-optimization
=========================
A Django package that provides mixins for optimizing querysets in Django REST Framework views and viewsets.

Features
--------
- Defer specific fields in queryset using class attributes.
- Include only specific fields in queryset using class attributes.

Installation
------------
pip install drf-queryset-optimization

Usage
-----
Using the optimization mixins in your viewsets is straightforward:

1. Import the `QuerysetOptimizationMixin` from `drf_queryset_optimization.mixins`.

2. In your viewset class, inherit from `QuerysetOptimizationMixin`.

3. Specify the fields you want to defer or include using the `defer_fields` and `only_fields` class attributes.

Example
-------
Here's a basic example of how you can use the package in your project:

```
from drf_queryset_optimization.mixins import QuerysetOptimizationMixin
from rest_framework.viewsets import ModelViewSet
from .models import YourModel
from .serializers import YourSerializer

class OptimizedModelViewSet(QuerysetOptimizationMixin, ModelViewSet):
    defer_fields = ["field1", "field2"]  # Fields to defer
    only_fields = []  # Fields to include

    queryset = YourModel.objects.all()
    serializer_class = YourSerializer
```

License
-------
MIT License
