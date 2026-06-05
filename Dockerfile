FROM python:3.11-slim

WORKDIR /app

ENV FLASK_APP=app6.py
ENV FLASK_ENV=production

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app6:app"]