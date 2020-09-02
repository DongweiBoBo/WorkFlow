from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Sample)
admin.site.register(Sequence)
admin.site.register(Assembly)
admin.site.register(Genemodel)
admin.site.register(Analyse)

