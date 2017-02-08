from celery import Celery
from tasks import app
from bulb import power_on, power_off
from celery.task.schedules import crontab
import time

app.conf.beat_schedule = {
    'alarm': {
        'task': 'alarm.alarm_mode',
        'schedule': 5.0
    }
}




@app.task
def set_alarm_time(hour, minute, day):
        print app.conf.beat_schedule['alarm']
        app.conf.beat_schedule['alarm'].update({'schedule': crontab(hour=hour,minute=minute,day_of_week=day)})
        print app.conf.beat_schedule['alarm']
        return


@app.task
def alarm_mode():
    counter = 1
    while counter < 100:
        counter += 1
        power_on(1.0,6500,200,0,0.01)
        sleep(1)
        power_off(0.01)