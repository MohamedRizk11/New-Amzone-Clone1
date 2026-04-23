from rest_framework import pagination

class mypagination(pagination.PageNumberPagination):
    page_size = 10
