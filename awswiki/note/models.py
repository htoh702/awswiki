from django.db import models

class note(models.Model):
    noteId = models.AutoField(primary_key=True)
    index = models.indexes
    tag = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=50, null=False)
    writer = models.CharField(max_length=10, null=False)
    content = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(max_length=50, auto_now=True)
    image = models.FileField(upload_to = 'note/images/', null=True)

    def __str__(self):
        return str(self.noteId)


class note_reviews(models.Model):
    noteReviewId = models.AutoField(primary_key=True)
    noteId = models.ForeignKey(note, on_delete=models.CASCADE)
    reivew = models.CharField(max_length=50)


    def __str__(self):
        return str(self.noteReviewId)