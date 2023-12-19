from django.db import models

class MyModel(models.Model):
    # json_data=models.JSONField(null=True, blank=True)
    # csv_data=models.TextField(null=True, blank=True)
    json_file=models.JSONField(null=True, blank=True)
    csv_file=models.TextField(null=True,blank=True)

