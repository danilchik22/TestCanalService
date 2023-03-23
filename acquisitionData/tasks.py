import logging

from GoogleTableScript.celery import celery_app

from acquisitionData.services import update_database

from celery.schedules import crontab

logger = logging.getLogger(__name__)

@celery_app.task
def update_base():
    logger.info("Ииииииихаааааа!!!")
    update_database()
    logger.info(f"Base update'")

    return None

celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.update_base',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
celery_app.conf.timezone = 'UTC'
