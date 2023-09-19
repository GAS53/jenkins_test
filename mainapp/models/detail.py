from django.db import models

from mainapp.models.base import DataTimeModel
from mainapp.models.assembly import Assembly


class Detail(DataTimeModel):
    name = models.CharField(verbose_name='название детали', max_length=50, default="")
    assembly = models.ForeignKey(Assembly, on_delete=models.DO_NOTHING, verbose_name='сборка', related_name='detail')
    

    class Meta:
        verbose_name = 'деталь'
        verbose_name_plural = 'детали'

    def __str__(self) -> str:
        return f'{self.id} {self.name}'