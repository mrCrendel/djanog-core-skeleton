from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            'results': data
        })

    def paginate_queryset(self, queryset, request, view=None):
        return super().paginate_queryset(queryset, request, view)


class ListPagination(PageNumberPagination):
    page_size = 10
