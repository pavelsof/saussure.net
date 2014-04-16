from django.contrib import admin

from problems.models import *


admin.site.register(Problem)
admin.site.register(ProblemChallenge)
admin.site.register(UserAttempt)
admin.site.register(Graph)

