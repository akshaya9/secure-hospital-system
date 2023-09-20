from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

GROUPS = ['patient', 'doctor', 'hospital_staff', 'lab_staff', 'insurance_staff', 'admin']


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        for group in GROUPS:
            Group.objects.get_or_create(name=group)
        print("Created default group and permissions.")
