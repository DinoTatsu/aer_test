from django.core.management.base import BaseCommand
from chronicle.models import Event, Chronicle


class Command(BaseCommand):
    help = 'Add data for tests'

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--chronicle',
            dest='chronicle',
            action='store_true',
            help='Add chronicle',
        )
        parser.add_argument(
            '-e',
            '--event',
            dest='event',
            action='store_true',
            help='Add events',
        )

    def create_chronicles(self):
        data = {
            'unique_id': '440AS-824942',
            'min_timestamp': '2021-05-24T02:00:00Z',
            'max_timestamp': '2021-06-15T02:00:00Z',
            'status': 'Open',
            'aircraft': '440AS',
        }
        Chronicle.objects.create(**data)

    def create_events(self):
        data = [
            {'unique_id': '440AS-924911', 'datetime': '2021-06-16T02:01:23Z', 'aircraft': '440AS'},
            {'unique_id': '440AS-924942', 'datetime': '2021-06-15T02:01:23Z', 'aircraft': '440AS'},
            {'unique_id': '440AS-924944', 'datetime': '2021-06-13T01:58:09Z', 'aircraft': '440AS'},
            {'unique_id': '440AS-924952', 'datetime': '2021-05-24T04:00:40Z', 'aircraft': '440AS'},
        ]
        for values in data:
            Event.objects.create(**values)

    def handle(self, *args, **options):
        if options['event']:
            try:
                self.create_events()
            except Exception:
                pass
        elif options['chronicle']:
            try:
                self.create_chronicles()
            except Exception:
                pass
        else:
            try:
                self.create_events()
                self.create_chronicles()
            except Exception:
                pass
