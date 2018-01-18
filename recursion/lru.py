

def get_from_cache(cache_key):
    """
    Returns a value from the cache
    Args:
    key
    Returns:
    value if present else None
    """
    try:
        # cache_list_location
        cache_list_location = cache[key]
        value = cache_list_location.value
    except KeyError:
        value = read_from_db(key)
        to_be_updated = True
    if value:
        if to_be_updated:
            if cache.capacity < MAX_CACHE_CAPACITY:
                cache[key] = current_tail
                current_tail.value = value
                current_tail.key = cache.key
                current_tail.prev.next = None
                current_tail.prev = None
                current_tail = cache_list_location
            else:
                return None
    # update the doubly linked list
    cache_list_location.prev.next = cache_list_location.next
    cache_list_location.next.prev = cache_list_location.prev
    cache_list_location.prev = None
    cache_list_location.next = current_head
    current_head.prev = cache_list_location`
