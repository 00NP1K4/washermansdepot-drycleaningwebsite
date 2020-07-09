from django.db import models

# Create your models here.
class Price(models.Model):
    item = models.CharField(max_length=200)
    Price = models.FloatField()

    def __str__(self):
        return self.item

class Testimonial(models.Model):
    image = models.ImageField(upload_to ='uploads')
    mini_image = models.ImageField(upload_to ='uploads')
    testimonial = models.TextField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Home_Carousel(models.Model):
    image = models.ImageField(upload_to ='uploads')
    phrase_in_span = models.CharField(max_length=200)
    phrase = models.CharField(max_length=200)

    def __str__(self):
        return self.phrase

class Step(models.Model):
    image = models.ImageField(upload_to ='uploads')
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Cert(models.Model):
    image = models.ImageField(upload_to ='uploads')
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label
class Service(models.Model):
    image1 = models.ImageField(upload_to ='uploads')
    label1 = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to ='uploads')
    label2 = models.CharField(max_length=200)
    image3 = models.ImageField(upload_to ='uploads')
    label3 = models.CharField(max_length=200)
    image4 = models.ImageField(upload_to ='uploads')
    label4 = models.CharField(max_length=200)

class Carousel(models.Model):
    image = models.ImageField(upload_to ='uploads')

class QuickQuotePrice(models.Model):
    item = models.CharField(max_length=200)
    Price = models.FloatField()

    def __str__(self):
        return self.item

class About(models.Model):
    aboutheading = models.TextField(max_length=1000)
    displayimage1 = models.ImageField(upload_to ='uploads')
    displayimage2 = models.ImageField(upload_to ='uploads')
    paragraph1 = models.TextField(max_length=1000)
    paragraph2 = models.TextField(max_length=1000)

class Contact(models.Model):
    contact_paragraph = models.TextField(max_length=1000)
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=200)
    social_fb = models.CharField(max_length=200)
    social_insta = models.CharField(max_length=200)
    social_twitter = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

class DryAndComm(models.Model):
    dry_para1 = models.TextField(max_length=1000)
    dry_para2 = models.TextField(max_length=1000)
    com_para1 = models.TextField(max_length=1000)
    com_para2 = models.TextField(max_length=1000)
    offer_item = models.CharField(max_length=200)
    offer_price = models.FloatField()
    pickup_image = models.ImageField(upload_to ='uploads')
    clean_image = models.ImageField(upload_to ='uploads')

class Laundromat(models.Model):
    paragraph = models.TextField(max_length=1000)
    image1 = models.ImageField(upload_to ='uploads')
    label1 = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to ='uploads')
    label2 = models.CharField(max_length=200)
    image3 = models.ImageField(upload_to ='uploads')
    label3 = models.CharField(max_length=200)
    image4 = models.ImageField(upload_to ='uploads')
    label4 = models.CharField(max_length=200)