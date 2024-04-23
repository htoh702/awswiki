from django.db import models

class Photo(models.Model):
    index = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='Photo/images/', null=True)

    def __str__(self):
        return f"Photo {self.index}"

class PhotoReview(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    review = models.CharField(max_length=50)

    def __str__(self):
        return f"Review {self.review} for Photo {self.photo.index}"  # Changed from self.photo.photo to self.photo.index
