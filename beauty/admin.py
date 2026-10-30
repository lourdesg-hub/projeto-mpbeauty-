
from django.contrib import admin

from .models import (
    Appointment,
    Availability,
    Package,
    Product,
    ProductReview,
    Professional,
    ProfessionalReview,
    Purchase,
    PurchaseItem,
    Service,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "stock",
        "active",
    )

    list_filter = (
        "category",
        "active",
    )

    search_fields = (
        "name",
        "description",
    )


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "profession",
        "city",
        "starting_price",
    )

    search_fields = (
        "name",
        "profession",
        "city",
    )

    inlines = [
        ServiceInline,
        AvailabilityInline,
    ]


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

    list_filter = (
        "status",
        "location",
        "date",
    )

    search_fields = (
        "client_name",
        "whatsapp",
    )


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "package_type",
        "price",
        "active",
    )

    list_filter = (
        "package_type",
        "active",
    )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "date",
    )


admin.site.register(PurchaseItem)
admin.site.register(ProductReview)
admin.site.register(ProfessionalReview)
admin.site.register(Service)
admin.site.register(Availability)
