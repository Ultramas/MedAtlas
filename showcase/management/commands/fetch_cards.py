
import requests
from django.core.management.base import BaseCommand
from showcase.models import Card

class Command(BaseCommand):
    help = 'Fetch Pokémon cards from the Pokémon TCG API'

    def handle(self, *args, **kwargs):
        api_url = 'https://api.pokemontcg.io/v2/cards'
        headers = {
            'X-Api-Key': 'POKEMON_API_KEY'  # Replace with your actual API key
        }
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            cards_data = response.json().get('data', [])
            for card_data in cards_data:
                card, created = Card.objects.update_or_create(
                    card_id=card_data['id'],
                    defaults={
                        'name': card_data.get('name'),
                        'supertype': card_data.get('supertype'),
                        'subtypes': ', '.join(card_data.get('subtypes', [])),
                        'hp': card_data.get('hp'),
                        'types': ', '.join(card_data.get('types', [])),
                        'evolves_to': ', '.join(card_data.get('evolvesTo', [])),
                        'rules': '\n'.join(card_data.get('rules', [])),
                        'attacks': '\n'.join([attack['name'] for attack in card_data.get('attacks', [])]),
                        'weaknesses': '\n'.join([weakness['type'] for weakness in card_data.get('weaknesses', [])]),
                        'retreat_cost': ', '.join(card_data.get('retreatCost', [])),
                        'set_name': card_data['set']['name'],
                        'set_series': card_data['set']['series'],
                        #'set_release_date': card_data['set'].get('releaseDate'),
                        'image_small': card_data['images']['small'],
                        'image_large': card_data['images']['large'],
                        'price': card_data.get('cardmarket', {}).get('prices', {}).get('averageSellPrice')
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added card: {card.name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated card: {card.name}'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from the Pokémon TCG API'))
