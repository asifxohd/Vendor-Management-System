from django.contrib import admin
from .models import HistoricalPerformance, PurchaseOrder


admin.site.register(HistoricalPerformance)
admin.site.register(PurchaseOrder)