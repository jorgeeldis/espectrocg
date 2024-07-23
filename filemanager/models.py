from django.db import models

# Create your models here.

def custom_upload_to(filename, file):
    # Get the file extension (e.g., 'png', 'pdf', 'csv')
    extension = filename.split('.')[-1].lower()
    # Map the extension to the correct folder
    if extension in ['png', 'pdf', 'csv']:
        return f'{extension}/{filename}'
    else: 
        # Default folder or handle unsupported file types
        return f'others/{filename}'

class Document(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to=custom_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename
