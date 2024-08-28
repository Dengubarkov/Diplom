from django.contrib.auth.models import User
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        account = UserSite.objects.create(
            user=username,
            email=user.email,
            name=user.name
        )





def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=UserSite)