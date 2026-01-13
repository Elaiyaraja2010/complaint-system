from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Open')

    def __str__(self):
        return self.subject
