from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'p' # Allows default name of page to be overriden
    page_size_query_param = 'size'
    max_page_size = 18
    last_page_strings = 'end'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit=5
    max_limit = 19
    # limit_query_param = 'max'   - can be used to override standard term of limit
    # offset_query_param = 'start' - can be used to override standard term of offset
    
class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = '-created'
    # cursor_query_param = 'record' - can be used to override standard term of cursor
