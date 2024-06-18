from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import products in Cosmetics'
    def handle(self, *args, **options):
        self.stdout.write("Importing products")
        