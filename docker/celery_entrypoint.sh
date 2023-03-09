echo "--> Starting celery process"
celery -A django_style_guide.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
