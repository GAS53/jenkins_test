from django.contrib import admin
from mainapp.models.user import BaseUser
from mainapp.models.assembly import Assembly
from mainapp.models.detail import Detail
from mainapp.models.material import Material
from mainapp.models.project import Project
from mainapp.models.stage import Stage


admin.site.register(BaseUser)
admin.site.register(Assembly)
admin.site.register(Detail)
admin.site.register(Material)
admin.site.register(Project)
admin.site.register(Stage)