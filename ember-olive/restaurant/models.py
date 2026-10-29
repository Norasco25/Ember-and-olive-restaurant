from django.db import models
class Reservation(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField()
    time=models.CharField(max_length=5)
    guests=models.PositiveSmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=12,choices=[('pending','Pending'),('confirmed','Confirmed'),('cancelled','Cancelled')],default='pending')
    def __str__(self): return f'{self.name} — {self.date} {self.time}'
