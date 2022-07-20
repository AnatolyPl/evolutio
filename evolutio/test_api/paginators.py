from rest_framework.pagination import CursorPagination


class CursorOrderPagination(CursorPagination):
    page_size = 2
    ordering = 'date_of_creation'
