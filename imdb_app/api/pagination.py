from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'p' # Allows default name of page to be overriden
    page_size_query_param = 'size'
    max_page_size = 18
    last_page_strings = 'end'


