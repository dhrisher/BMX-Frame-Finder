from django.db import models


# Create your models here.


class FrameSize(models.Model):
    size = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.size)


class Frame(models.Model):
    name = models.CharField(max_length=50)
    chainstay = models.DecimalField(max_digits=4, decimal_places=1)
    seat_tube_angle = models.DecimalField(max_digits=4, decimal_places=1)
    head_tube_angle = models.DecimalField(max_digits=4, decimal_places=1)
    frame_pic = models.ImageField(upload_to='frame_pics', blank=False)
    link = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.ManyToManyField(FrameSize)
    chainstay_processed = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    seat_tube_processed = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    head_tube_processed = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    discipline_average = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    suitability = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.frame_pic.url
        except:
            url = ''
        return url
