from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, verbose_name='بیوگرافی کوتاه')
    total_score = models.IntegerField(default=0, verbose_name='امتیاز کل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username

    @property
    def rank_title(self):
        score = self.total_score
        if score >= 1000:
            return 'Legend 🏆'
        elif score >= 500:
            return 'Game Master 🎖️'
        elif score >= 200:
            return 'Pro ⚔️'
        elif score >= 50:
            return 'Amateur 🎮'
        return 'Newbie 🌱'