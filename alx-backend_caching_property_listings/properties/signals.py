from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Property

@receiver(post_save, sender=Property, dispatch_uid='invalidate_property_cache_on_save')
def invalidate_property_cache_on_save(sender, instance, **kwargs):
    try:
        if instance.pk:
            cache.delete('all_properties')
    except Exception as e:
        print(f"Error deleting cache for Property {instance.pk}: {e}")

@receiver(post_delete, sender=Property, dispatch_uid='invalidate_property_cache_on_delete')
def invalidate_property_cache_on_delete(sender, instance, **kwargs):
    try:
        if instance.pk:
            cache.delete('all_properties')
    except Exception as e:
        print(f"Error deleting cache for Property {instance.pk}: {e}")