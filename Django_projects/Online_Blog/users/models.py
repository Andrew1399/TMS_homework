from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Reader(models.Model):
    """A simple model of a reader who learns information
    in the blog.
    """
    class Meta:
        verbose_name = _('Reader')
        verbose_name_plural = _('Readers')

    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reader'
    )
    username = models.CharField(_('username'), max_length=50, blank=True)
    email = models.EmailField(_('email'), null=True, blank=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"Reader {self.username} "

class Writer(models.Model):
    """A model of a writer who can create own posts
    and own content.
    """
    class Meta:
        verbose_name = _('Writer')
        verbose_name_plural = _('Writers')

    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='writer'
    )
    username = models.CharField(_('username'), max_length=50, blank=True)
    email = models.EmailField(_('email'), null=True, blank=True)
    company = models.CharField(_('company'), max_length=60, blank=True)
    type_of_activity = models.CharField(_('type of activity'), max_length=70, blank=True)
    type_of_blog = models.CharField(_('type of blog'), max_length=50, blank=True)

    def __str__(self):
        return f"Writer {self.username}"
