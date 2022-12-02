from django.db import models

# Create your models here.


class Joined_Channels(models.Model):
    channel_name = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=200)

    def __str__(self):
        return self.channel_name


class Job_catagories(models.Model):
    channel = models.ForeignKey(Joined_Channels, on_delete=models.CASCADE)
    catagory_name = models.CharField(max_length=200)
    catagory_filtering_words = models.TextField()

    def __str__(self):
        return self.catagory_name


class Jobs(models.Model):
    catagory_id = models.ForeignKey(Job_catagories, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, default="")
    job_name = models.CharField(max_length=200)
    job_name_arabic = models.CharField(max_length=200, default='')
    job_url = models.URLField()
    job_date = models.DateField(auto_now=True)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.job_name
