from django.contrib import admin

from problems.models import *


admin.site.register(LanguageFamily)
admin.site.register(Tag)
admin.site.register(Problem)
admin.site.register(Graph)
admin.site.register(Challenge)
admin.site.register(Attempt)

