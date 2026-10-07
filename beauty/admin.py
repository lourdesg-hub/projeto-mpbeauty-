from django.contrib import admin

# Register your models here.

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


admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.register(ProductReview)
admin.site.register(Professional)
admin.site.register(Service)
admin.site.register(Availability)
admin.site.register(Appointment)
admin.site.register(ProfessionalReview)
admin.site.register(Package)