"""Instantiates celery app."""
from celery import Celery

# instantiate celery instance
app = Celery(
    'celery_config',
    broker='redis://localhost:6379/0',
    include=['tldr_slackbot.bot']
)

