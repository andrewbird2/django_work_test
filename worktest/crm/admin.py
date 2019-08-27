from django.contrib import admin

from worktest.crm.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ["email", "name"]
    list_display = ["email", "name"]
    search_fields = ["email", "name"]
