from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import SiteSetting
from utils.media_cleanup import delete_old_file_on_update, delete_file_on_delete

@receiver(pre_save, sender=SiteSetting)
def update_setting_images(sender, instance, **kwargs):
    delete_old_file_on_update(instance, SiteSetting, 'logo')
    delete_old_file_on_update(instance, SiteSetting, 'favicon')

@receiver(post_delete, sender=SiteSetting)
def delete_setting_images(sender, instance, **kwargs):
    delete_file_on_delete(instance, 'logo')
    delete_file_on_delete(instance, 'favicon')
