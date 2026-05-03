FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask flask-socketio

EXPOSE 5000

CMD ["python", "app.py"]