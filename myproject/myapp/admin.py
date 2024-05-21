from django.contrib import admin
from myapp.models import Contact
from myapp.models import Appointment
from myapp.models import Bookings

# Register your models here.
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Bookings)


