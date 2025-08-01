from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver #This is a decorator that connects a function to a signal.
from .models import Blog
from utils.media_cleanup import delete_old_file_on_update, delete_file_on_delete

@receiver(pre_save, sender=Blog)
def blog_image_update_cleanup(sender, instance, **kwargs):
    delete_old_file_on_update(instance, Blog, 'blog_image')

@receiver(post_delete, sender=Blog)
def blog_image_delete_cleanup(sender, instance, **kwargs):
    delete_file_on_delete(instance, 'blog_image')
