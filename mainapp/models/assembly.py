from django.db import models


from mainapp.models.base import DataTimeModel
from mainapp.models.project import Project


class Assembly(DataTimeModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(verbose_name='описание проекта', max_length=36, default="")
    
    

    class Meta:
        verbose_name = 'сборка'
        verbose_name_plural = 'сборки'

    def __str__(self) -> str:
        return f'{self.id} {self.description[:10]}'  # в выводе название обрезано