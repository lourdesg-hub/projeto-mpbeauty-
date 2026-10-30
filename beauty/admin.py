from django.contrib import admin
from .models import (
    Product,
    Purchase,
    PurchaseItem,
    ProductReview,
    Professional,
    Service,
    Availability,
    Appointment,
    ProfessionalReview,
    Package,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "active")
    list_filter = ("category", "active")
    search_fields = ("name",)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "date")


@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ("purchase", "product", "quantity")


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "created_at")


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("name", "profession", "city", "experience_years")
    search_fields = ("name", "profession", "city")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "professional", "price", "duration")


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("professional", "weekday", "start_time", "end_time")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "client_name",
        "professional",
        "service",
        "date",
        "time",
        "status",
    )
    list_filter = ("status", "location", "date")
    search_fields = ("client_name", "whatsapp")


@admin.register(ProfessionalReview)
class ProfessionalReviewAdmin(admin.ModelAdmin):
    list_display = ("professional", "user", "rating", "created_at")


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "package_type", "price", "active")
    list_filter = ("package_type", "active")
    search_fields = ("name",)