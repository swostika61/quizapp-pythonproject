import json
from django.core.management.base import BaseCommand
from quiz_app.models import Questions  # Adjust the import according to your model

class Command(BaseCommand):
    help = 'Load questions from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file containing questions')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            questions = json.load(file)
            for question_data in questions:
                Questions.objects.create(**question_data)
        self.stdout.write(self.style.SUCCESS('Successfully loaded questions'))