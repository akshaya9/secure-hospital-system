from django.contrib import admin

from .models import (Appointment, Diagnosis, Doctor, Insurance, Patient,
                     Payment, Test)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass
