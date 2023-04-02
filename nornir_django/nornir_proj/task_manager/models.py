from django.db import models

# Create your models here.
class ExecutionEvents(models.Model):
  index          = models.AutoField(primary_key=True)
  timestamp      = models.DateTimeField(auto_now_add=True)
  event_name     = models.CharField('event name', max_length=255)
  event_message  = models.CharField('event message', max_length=255)
  class Meta:
    db_table = 'events'
    managed  = True

class ExecutionResults(models.Model):
  index     = models.AutoField(primary_key=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  name      = models.CharField('name of task execution', max_length=255)
  hosts     = models.CharField('list of hosts for this execution', max_length=255)
  results   = models.TextField('json  string for execution')
  class Meta:
    db_table = 'results'
    managed  = True
