
from django.core.management.base import BaseCommand
import nltk

class Command(BaseCommand):
    help = 'Download NLTK data'

    def handle(self, *args, **kwargs):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('brown')
        nltk.download('wordnet')
        nltk.download('punkt_tab')
        self.stdout.write(self.style.SUCCESS('NLTK data downloaded!'))
