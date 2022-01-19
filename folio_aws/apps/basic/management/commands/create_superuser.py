from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent.parent

SETTINGS = None
with open(BASE_DIR.parent.parent.parent.parent
          / 'tmp/folio-env-app-config.json') as f:
    SETTINGS = json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(
                username=SETTINGS['SUPER_USERNAME']).exists():
            User.objects.create_superuser(SETTINGS['SUPER_USERNAME'],
                                          SETTINGS['SUPER_EMAIL'],
                                          SETTINGS['SUPER_PWORD'])
