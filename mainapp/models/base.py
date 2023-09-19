from django.db import models


class AbstractManager(models.Manager):  # если нужны общие обработчики
    
    def get_queryset(self):
        return super().get_queryset().all()
    
class DataTimeModel(models.Model):
    id = models.PositiveBigIntegerField(db_index=True, primary_key=True, unique=True, auto_created=True, editable=False)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, editable=False)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, editable=False)
    is_deleted = models.BooleanField(verbose_name='Запись удалена', default=False)

    objects = AbstractManager()

    def delete(self, *args, **kwargs):
            self.is_deleted = True
            self.save()

    class Meta:
        ordering = ('-created',)
        abstract = True