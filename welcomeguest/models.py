from django.db import models


class Guest(models.Model):

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True
    )

    YES = "Да"
    NO = "Нет"

    CHOICES = [
        (YES, "Да"),
        (NO, "Нет"),
    ]

    full_name = models.CharField(
        max_length=200,
        verbose_name="ФИО"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон"
    )

    attendance = models.CharField(
        max_length=10,
        choices=CHOICES,
        verbose_name="Придет"
    )

    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий"
    )

    wish = models.TextField(
        blank=True,
        verbose_name="Пожелание"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    extra_guests = models.TextField(
        blank=True,
        verbose_name="Добавленные гости"
    )

    guest_count = models.PositiveIntegerField(
        default=1,
        verbose_name="Всего гостей"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"
    def save(self, *args, **kwargs):

        if self.extra_guests.strip():
            self.total_guests = len(self.extra_guests.strip().split("\n")) + 1
        else:
            self.total_guests = 1

        super().save(*args, **kwargs)