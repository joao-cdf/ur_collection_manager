#!/bin/sh
source virtual/bin/activate
exec gunicorn -b :5000  --access-logfile - --error-logfile - --config=gunicorn_config.py collection_manager:flask_app