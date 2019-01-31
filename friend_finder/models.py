from django.db import models


class User(models.Model):
    installation_id = models.TextField(unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def get(self):
        return {"id": self.id, "installation_id": self.installation_id, "longitude": self.longitude, "latitude": self.latitude}

class Group(models.Model):
    name = models.TextField(unique=True)
    active = models.BooleanField()

    def get(self):
        return {"id": self.id, "name": self.name, "active": self.active}


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)