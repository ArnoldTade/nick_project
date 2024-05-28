from django.db import models


class Booking(models.Model):
    EVENT_TYPES = [
        ("Wedding", "Wedding"),
        ("Birthday", "Birthday"),
        ("Corporate", "Corporate"),
        ("Anniversary", "Anniversary"),
        ("Graduation", "Graduation"),
        ("Conference", "Conference"),
    ]

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Overdue", "Overdue"),
    ]

    EVENT_STATUS = [
        ("Upcoming", "Upcoming"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    #booking_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    contact_information = models.TextField()
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    design_service = models.BooleanField(default=False)
    number_of_guests = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    downpayment = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)
    event_status = models.CharField(max_length=20, choices=EVENT_STATUS)

    def __str__(self):
        return f"Booking {self.client_name}"
