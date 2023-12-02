from django.core.management.base import BaseCommand
from faker import Faker
from apps.core.models import Print, User
from random import choice

class Command(BaseCommand):
    help = 'Load initial data'

    def handle(self, *args, **options):
        faker = Faker('pt_BR')
        roles = ['Professor', 'Aluno', 'Servidor']
        
        users = [User(
            username=faker.user_name(),
            email=faker.email(),
            preferred_email=faker.email(),
            google_classroom_email=faker.email(),
            usual_name=faker.name(),
            password=faker.password(),
            full_name=faker.name(),
            first_name = faker.name(),
            last_name = faker.name(),
            identification = faker.user_name(),
            role = choice(roles)
        ) for _ in range(10)]
        
        User.objects.bulk_create(users)
        
        prints = [Print(
            attachment = faker.file_name(),
            created_by = choice(users),
            print_count = faker.random_int(min=1, max=100),
            observation = faker.text(),
            withdraw_date = faker.date(),
            withdraw_time = faker.time(),
            status = choice(['printed', 'withdrawn', 'pending']),
            withdrawn_at = choice([faker.date(), None])
        ) for _ in range(50)]
        
        Print.objects.bulk_create(prints)
        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully'))
        
        