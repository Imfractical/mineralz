"""Command that populates database from a specially-formatted JSON file"""
import json

from django.core.management.base import BaseCommand, CommandError

from mineral_catalog.models import Mineral


class Command(BaseCommand):
    help = "Populates database using an included JSON file"

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def _populate(self, json_file):
        try:
            mineral_file = open(json_file, 'r', encoding='utf8')
        except OSError:
            raise CommandError("{} could not be opened").format(json_file)

        mineral_data = json.load(mineral_file)
        for dictionary in mineral_data:
            new_mineral = Mineral()
            for key in dictionary:
                field = key.replace(' ', '_')
                setattr(new_mineral, field, dictionary[key])
            new_mineral.save()

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        self._populate(json_file)

        self.stdout.write(self.style.SUCCESS("Successfully populated database"))
