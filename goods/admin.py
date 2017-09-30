from django.contrib import admin
from .models import Good, Discount_code


class Dicount_codeAdmin(admin.ModelAdmin):
    list_display = ["customer", "good", "staff", "date_of_issue"]
    list_filter = ["customer", "good"]


admin.site.register(Good)
admin.site.register(Discount_code, Dicount_codeAdmin)
