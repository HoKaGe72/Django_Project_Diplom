from django.contrib import admin
from .models import md_chapter, MdMethodicalSolution, MdDivision, MdPeriod, MdResponsible

admin.site.register(md_chapter)
admin.site.register(MdMethodicalSolution)
admin.site.register(MdDivision)
admin.site.register(MdPeriod)
admin.site.register(MdResponsible)
admin.site.site_url = "/home"

# Register your models here.
