from celery.task import task
from celery import Celery
from celery.schedules import crontab
from celery.bin import worker
from weather import sunrise_sunset
from brightness import kelvin, brightness
from bulb import power_on,power_off


app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.timezone = 'Europe/London'

app.conf.update(worker_pool_restarts=True)

from automated import lights
@app.task
def new_w():
    argv = ['celery','-A','automated','--loglevel=DEBUG','-B', '--hostname=worker2@dbc']
    app.worker_main(argv)
    return

@app.task
def off():
    app.control.broadcast('shutdown',destination=['worker2@dbc'])
    power_off()
