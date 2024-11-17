from django.db import models
from django.contrib.auth.models import User


class Grievance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    product_purchased = models.CharField(max_length=255)
    issue_faced = models.TextField()
    file_upload = models.FileField(upload_to='grievances/')  # Files saved in "media/grievances/"
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product_purchased}"
