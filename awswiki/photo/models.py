from django.db import models

class photo(models.Model):
    index = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(max_length=50, auto_now=True)
    image = models.FileField(upload_to = 'photo/images/', null=True)

    def __str__(self):
        return str(self.photoId)


class photo_reviews(models.Model):
    photoReviewId = models.AutoField(primary_key=True)
    index = models.ForeignKey(photo, on_delete=models.CASCADE)
    reivew = models.CharField(max_length=50)


    def __str__(self):
        return str(self.photoReviewId)
