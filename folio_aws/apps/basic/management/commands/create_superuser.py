import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='admin-liam').exists():
            User.objects.create_superuser('admin-liam',
                                          'liamegancontact@gmail.com',
                                          'folioAdminEggMan15!')