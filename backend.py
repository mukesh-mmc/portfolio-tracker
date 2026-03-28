_cache_timestamp = {}
CACHE_TTL = 3600  # TTL in seconds

def _is_cache_valid(key):
    """Check if the cached data is still valid based on timestamps."""
    if key in _cache_timestamp:
        cache_time = _cache_timestamp[key]
        return (current_time - cache_time) <= CACHE_TTL
    return False

# Example update in the _fetch_nav_history function

def _fetch_nav_history():
    """ Fetch NAV history, using cache if available. """
    key = 'nav_history'
    if _is_cache_valid(key):
        log(f'Cache hit for {key}. Cache age: {current_time - _cache_timestamp[key]} seconds.')
        return cache
    else:
        log(f'Cache expired for {key}, fetching new data.')
        # Fetch new data and update cache
        _cache_timestamp[key] = current_time
        return new_data

# Example update in the get_nav_data function

def get_nav_data():
    """ Get NAV data, using cache if available. """
    key = 'nav_data'
    if _is_cache_valid(key):
        log(f'Cache hit for {key}. Cache age: {current_time - _cache_timestamp[key]} seconds.')
        return cache
    else:
        log(f'Cache expired for {key}, fetching new data.')
        # Fetch new data and update cache
        _cache_timestamp[key] = current_time
        return new_data