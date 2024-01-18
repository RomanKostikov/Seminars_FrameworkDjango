from django.core.management.base import BaseCommand, CommandParser

from app_1.models import Author


class Command(BaseCommand):
    help = 'Deletes an author by id'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Author id to delete')

    def handle(self, *args, **kwargs) -> str | None:
        id = kwargs['id']

        author = Author.objects.filter(pk=id).first()

        author.delete()
        self.stdout.write(self.style.ERROR(f'Deleted author: {author}'))
