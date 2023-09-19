from django.db import models

from mainapp.models.base import DataTimeModel
from mainapp.models.user import BaseUser


class Stage(DataTimeModel):
    name = models.CharField(verbose_name='название', max_length=36, default="")
    description = models.CharField(max_length=50, verbose_name='описание', default="")
    creator = models.ForeignKey(BaseUser, verbose_name='создатель стадии', on_delete=models.DO_NOTHING, related_name='stage_creator')
    responsible_worker = models.ForeignKey(BaseUser, verbose_name='исполнитель стадии', on_delete=models.DO_NOTHING, related_name='stage_worker')

    class Meta:
        verbose_name = 'стадия'
        verbose_name_plural = 'стадии'

    def __str__(self) -> str:
        return f'{self.id} {self.shot_name}'