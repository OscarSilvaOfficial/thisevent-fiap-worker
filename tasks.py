from celery import Celery
import requests

app = Celery('user')

app.config_from_object('celeryconfig')

@app.task(name='create-user')
def create_user(user):
  return requests.post('http://localhost:5001/api/users', json=user)