from django.db import models

class job(models.Model):
    jobId = models.AutoField(primary_key=True)
    index = models.indexes 
    tag = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=50, null=False)
    writer = models.CharField(max_length=10, null=False)
    content = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(max_length=50, auto_now=True)
    image = models.FileField(upload_to = 'job/images/', null=True)

    def __str__(self):
        return str(self.jobId)


class job_reviews(models.Model):
    jobReviewId = models.AutoField(primary_key=True)
    jobId = models.ForeignKey(job, on_delete=models.CASCADE)
    reivew = models.CharField(max_length=50)


    def __str__(self):
        return str(self.jobReviewId)
