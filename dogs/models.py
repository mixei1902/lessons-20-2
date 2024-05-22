from django.db import models


class Breed(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Нахвание породы",
        help_text="Введите название породы",
    )
    description = models.TextField(
        verbose_name="Описание породы",
        help_text="Введите описание породы",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
        # ordering = ['name']

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="кличка собаки", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="порода",
        help_text="Введите породу собаки",
        blank=True,
        null=True,
        related_name='dogs',
    )
    picture = models.ImageField(
        upload_to="dogs/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
    )
    date_born = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
        help_text="Укажите дату рождения",
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]

    def __str__(self):
        return self.name
