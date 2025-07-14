from django.core import cache
import logging
from django.core.cache import cache
from redis import get_redis_connection

def get_all_properties():
    try:
        # Attempt to retrieve properties from cache
        # Assuming 'cache' is a Django cache instance
        # If using Redis, ensure the cache backend is configured correctly
    properties = cache.get('all_properties')
        if properties is None:
            properties = Property.objects.all()
            cache.set('all_properties', properties, timeout=3600)  # Cache for 10 minutes
        return properties
    except Exception as e:
        print(f"Error fetching properties: {e}")
        return None
def property_list(request):
    try:
        # Fetch properties using the utility function
        # This will either return cached properties or fetch from the database
    properties = get_all_properties()
        if properties is None:
            return HttpResponse("Error fetching properties", status=3600)
    except Exception as e:
        print(f"Error rendering property list: {e}")
        return HttpResponse("Internal Server Error", status=3600)

def get_redis_cache_metrics():
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()
        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total = hits + misses
        hit_ratio = (hits / total_requests) if total_requests > 0 else 0
        metrics = {
            'hits': hits,
            'misses': misses,
            'hit_ratio': hit_ratio,
        }
        logging.info(f"Redis Cache Metrics: {metrics}")
        return metrics
    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {'hits': 0, 'misses': 0, 'hit_ratio': 0.0}
