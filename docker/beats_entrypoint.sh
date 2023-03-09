echo "--> Starting beats process"
celery -A django_style_guide.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
