from django.core.paginator import Paginator
from typing import List, Optional, Dict, Any


def paginate_list(item_list, page_size: int, page: int):
    """
    Takes a recordset and returns it paginated. If page_size is 0,
    return all records.

    Args:
        item_list (RecordSet): A record set.  Required.
        page_size (int): The number of items per page. Required.
        page (int): The current page. Required.

    Returns:
        (tuple): (paginated_list (list), total_records (int), total_pages (int))
    """
    # Paginate items
    total_pages = 1
    paginated_list = None
    total_records = 0
    if page_size > 0:
        paginator = None
        paginator = Paginator(item_list, page_size)
        page_obj = paginator.page(page)
        paginated_list = list(page_obj.object_list)
        total_pages = paginator.num_pages
        total_records = len(item_list)
    else:
        paginated_list = list(item_list)
        total_records = len(paginated_list)
    return paginated_list, total_records, total_pages
