import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(DJANGO_BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.TIME_ZONE = 'UTC'

django.setup()

if __name__ == '__main__':
  import faker
  from contact.models import Category, Contact

  Contact.objects.all().delete()
  Category.objects.all().delete()

  fake = faker.Faker('pt_BR')
  categories = ['Amigos', 'Família', 'Trabalho', 'Conhecidos']

  django_categories = [Category(name=category) for category in categories]

  for category in django_categories:
    category.save()

  django_contacts = []

  for _ in range(NUMBER_OF_OBJECTS):
    profile = fake.profile()
    email = profile['mail']
    first_name, last_name = profile['name'].split(' ', 1)
    phone = f'+55 (98) {fake.random_number(digits=9)}'
    created_at = datetime - fake.date_this_year()
    description = fake.text(max_nb_chars=100)
    category = choice(django_categories)

    django_contacts.append(Contact(
      first_name=first_name,
      last_name=last_name,
      email=email,
      phone=phone,
      description=description,
      category=category,
      created_at=created_at
    ))

  if len(django_contacts) > 0:
    Contact.objects.bulk_create(django_contacts)
    print(f'Created {len(django_contacts)} contacts')
    

  

