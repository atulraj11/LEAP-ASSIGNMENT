# tasks.py

import logging
from celery import shared_task
import requests
from .models import CatFact

@shared_task
def fetch_cat_facts_task():
    try:
        response = requests.get('https://cat-fact.herokuapp.com/facts')
        response.raise_for_status()
        logging.warning(response)
        data = response.json()
        text = data[0]['text']
        CatFact.objects.create(fact=text)
        return True
    except Exception as e:
        print(f"Error fetching cat fact: {str(e)}")
        return False
