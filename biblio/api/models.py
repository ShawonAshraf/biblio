from django.db import models
import uuid
import json


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        json_obj = {"id": str(self.id), "name": self.name}
        return json.dumps(json_obj)


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        json_obj = {"id": str(self.id), "name": self.name}
        return json.dumps(json_obj)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        json_obj = {
            "id": str(self.id),
            "name": self.name,
            "author": str(self.author),
            "language": str(self.language),
            "isbn": self.isbn,
        }
        return json.dumps(json_obj)
