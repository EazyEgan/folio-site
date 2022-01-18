import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import subprocess
import ast

# Unfortunately EB won't access variables stored in environment so must do the
# below
def get_environ_vars():
    completed_process = subprocess.run(
        ['/opt/elasticbeanstalk/bin/get-config', 'environment'],
        stdout=subprocess.PIPE,
        text=True,
        check=True
    )
    return ast.literal_eval(completed_process.stdout)


BASE_DIR = Path(__file__).resolve().parent.parent
env_vars = get_environ_vars()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(
                username=env_vars['SUPER_USERNAME']).exists():
            User.objects.create_superuser(env_vars['SUPER_USERNAME'],
                                          env_vars['SUPER_EMAIL'],
                                          env_vars['SUPER_PWORD'])
