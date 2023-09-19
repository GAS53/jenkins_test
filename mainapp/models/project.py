from django.db import models

from mainapp.models.stage import Stage
from mainapp.models.base import DataTimeModel

class Project(DataTimeModel):
    description = models.CharField(verbose_name='описание проекта', max_length=50, default="")
    is_deleted = models.BooleanField(verbose_name='проект удален')
    is_immutable = models.BooleanField(verbose_name='неизменяемый(после сдачи в архив)')
    now_stage = models.ForeignKey(Stage, related_name='stage', on_delete=models.DO_NOTHING)
    


    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self) -> str:
        return f'{self.id} {self.description[:10]}'  # в выводе название обрезано