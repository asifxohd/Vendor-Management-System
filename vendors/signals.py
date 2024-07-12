from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q, F, Sum
from purchase_orders.models import PurchaseOrder, HistoricalPerformance
from .models import Vendor
from django.utils import timezone

@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    vendor = instance.vendor
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_deliveries = completed_orders.filter(Q(delivery_date__gte=F('acknowledgment_date'))).count()
    on_time_delivery_rate = (on_time_deliveries / completed_orders.count()) * 100 if completed_orders.exists() else 0

    if created:
        vendor.on_time_delivery_rate = on_time_delivery_rate

        total_quality_ratings = completed_orders.aggregate(total=Sum('quality_rating'))['total']
        vendor.quality_rating_avg = total_quality_ratings / completed_orders.count() if total_quality_ratings else 0

        acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
        if acknowledged_orders.exists():
            total_response_time = acknowledged_orders.aggregate(
                total=Sum(F('acknowledgment_date') - F('issue_date'))
            )['total']
            vendor.average_response_time = (total_response_time.total_seconds() / acknowledged_orders.count() / 3600) / 24
        else:
            vendor.average_response_time = 0

    else:
        vendor.on_time_delivery_rate = on_time_delivery_rate

        total_quality_ratings = completed_orders.aggregate(total=Sum('quality_rating'))['total']
        vendor.quality_rating_avg = total_quality_ratings / completed_orders.count() if total_quality_ratings else 0

        acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
        if acknowledged_orders.exists():
            total_response_time = acknowledged_orders.aggregate(
                total=Sum(F('acknowledgment_date') - F('issue_date'))
            )['total']
            vendor.average_response_time = (total_response_time.total_seconds() / acknowledged_orders.count() / 3600) / 24
        else:
            vendor.average_response_time = 0

        HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=vendor.quality_rating_avg,
            average_response_time=vendor.average_response_time,
            fulfillment_rate=(completed_orders.count() / PurchaseOrder.objects.filter(vendor=vendor).count()) * 100
        )

    vendor.fulfillment_rate = (completed_orders.count() / PurchaseOrder.objects.filter(vendor=vendor).count()) * 100
    vendor.save()
