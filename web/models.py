from django.db import models

# Create your models here.

class User(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)


class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_num = models.IntegerField()
    submit_num = models.IntegerField()


class JobSubmission(models.Model):
    job_submission_id = models.IntegerField(primary_key=True)
    student_id = models.IntegerField()
    sub_time = models.DateTimeField()
    job_id = models.IntegerField()
    file_name = models.CharField(max_length=255)





