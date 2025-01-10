from django.db import models


# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null=False)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email + ' - ' + self.message

# Changelog Model
class Changelog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.description + ' - ' + str(self.date)