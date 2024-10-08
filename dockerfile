FROM python:3.8

WORKDIR /app

COPY ./AgendaApp/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./AgendaApp /app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
