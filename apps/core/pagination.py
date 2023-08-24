""" Pagination classes for the API. """
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    """Pagination class for large result sets."""

    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class StandardResultsSetPagination(PageNumberPagination):
    """Pagination class for standard result sets."""

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50
