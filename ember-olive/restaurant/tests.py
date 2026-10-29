from datetime import timedelta
from django.test import TestCase,Client
from django.utils import timezone
from .models import Reservation
class BookingTests(TestCase):
    def data(self):
        date=timezone.localdate()+timedelta(days=1)
        while date.weekday()==0: date+=timedelta(days=1)
        return dict(name='Test Guest',email='test@example.com',date=date.isoformat(),time='18:00',guests=2)
    def test_home_and_pending_booking(self):
        self.assertContains(self.client.get('/'),'Ember & Olive')
        self.assertEqual(self.client.post('/reserve/',self.data()).status_code,201)
        self.assertEqual(Reservation.objects.get().status,'pending')
    def test_invalid_date_and_party(self):
        data=self.data();data['date']=(timezone.localdate()-timedelta(days=1)).isoformat();data['guests']=99
        self.assertEqual(self.client.post('/reserve/',data).status_code,400)
        self.assertFalse(Reservation.objects.exists())
    def test_csrf_and_method(self):
        self.assertEqual(Client(enforce_csrf_checks=True).post('/reserve/',self.data()).status_code,403)
        self.assertEqual(self.client.get('/reserve/').status_code,405)
