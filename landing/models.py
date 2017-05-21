from django.db import models



class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return "Пользователь %s %s %s %s %s" % (self.name, self.email, self.phone, self.city, self.comment,)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'

