from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *
# Register your models here.
admin.site.register(Solution, TranslatableAdmin)
admin.site.register(Service, TranslatableAdmin)
admin.site.register(Contact)