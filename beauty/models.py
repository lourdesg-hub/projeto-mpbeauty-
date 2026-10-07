
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('maquiagem', 'Maquiagem'),
        ('skincare', 'Skin Care'),
        ('cabelo', 'Cabelo'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(default=0)
    image = models.URLField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra de {self.user.username}'


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class Professional(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    bio = models.TextField()
    experience_years = models.PositiveIntegerField(default=0)
    home_service = models.BooleanField(default=False)
    studio_service = models.BooleanField(default=True)
    starting_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.profession}'


class Service(models.Model):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='services'
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.name} - {self.professional.name}'


class Availability(models.Model):
    WEEKDAYS = [
        (0, 'Segunda-feira'),
        (1, 'Terça-feira'),
        (2, 'Quarta-feira'),
        (3, 'Quinta-feira'),
        (4, 'Sexta-feira'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]

    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='availabilities'
    )
    weekday = models.IntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return (
            f'{self.professional.name} - '
            f'{self.get_weekday_display()}'
        )


class Appointment(models.Model):
    LOCATION_CHOICES = [
        ('studio', 'No estabelecimento'),
        ('home', 'Atendimento a domicílio'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmado'),
        ('cancelled', 'Cancelado'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )
    location = models.CharField(
        max_length=10,
        choices=LOCATION_CHOICES
    )
    date = models.DateField()
    time = models.TimeField()
    client_name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'{self.client_name} - '
            f'{self.service.name} - '
            f'{self.date}'
        )


class ProfessionalReview(models.Model):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('professional', 'user')

    def __str__(self):
        return f'{self.user.username} - {self.professional.name}'


class Package(models.Model):
    PACKAGE_TYPES = [
        ('client', 'Cliente'),
        ('bride', 'Noiva'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    package_type = models.CharField(
        max_length=10,
        choices=PACKAGE_TYPES
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name