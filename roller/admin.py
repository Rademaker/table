from django.contrib import admin
from roller.models import Table, RandomPick



class RandomPickInline(admin.TabularInline):
	model = RandomPick
	fields = ['start_value','end_value','text']


class TableAdmin(admin.ModelAdmin):
	inlines = [RandomPickInline]

admin.site.register(Table, TableAdmin)
