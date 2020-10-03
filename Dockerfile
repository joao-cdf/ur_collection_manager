FROM python:3.8-alpine

RUN adduser -D ur

WORKDIR /home/ur

COPY requirements.txt requirements.txt
RUN python -m venv virtual
RUN virtual/bin/pip install --upgrade pip
RUN virtual/bin/pip install -r requirements.txt

COPY app app
COPY collection_manager.py config.py gunicorn_config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP collection_manager.py

RUN chown -R ur:ur ./
USER ur

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]