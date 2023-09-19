from django.db import models

from mainapp.models.base import DataTimeModel
from mainapp.models.detail import Detail


class Material(DataTimeModel):
    name = models.CharField(verbose_name='название материала', max_length=36, default="")
    detail = models.ForeignKey(Detail, on_delete=models.DO_NOTHING, verbose_name='материал', related_name='material')
    

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

    def __str__(self) -> str:
        return f'{self.id} {self.name}'