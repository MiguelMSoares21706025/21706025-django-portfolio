from django.contrib import admin
from .models import *

# Register your models here.
class CurricularUnitAdmin(admin.ModelAdmin):
    list_display = ('curricular_unit',
                    'link',
                    'year',
                    'semester',
                    'ects',
                    'responsible_teacher',
                    'additional_teacher',
                    'ranking',
                    'academic')

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Certification)
admin.site.register(OtherCourse)
admin.site.register(Teacher)
admin.site.register(Academic)
admin.site.register(CurricularUnit, CurricularUnitAdmin)
admin.site.register(Project)
admin.site.register(Tech_BackEnd)
admin.site.register(Tech_FrontEnd)
admin.site.register(Tech_Other)
admin.site.register(Subject)