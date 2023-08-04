from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    images = models.ImageField(upload_to='midea/images/')
    number_id = models.IntegerField()

    def __str__(self):
        return self.title


class Category_product(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.ForeignKey(Category_product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='midea/product/')
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=7000)
    images_statis = models.ImageField(upload_to='midea/statis_product/')

    def __str__(self):
        return self.title


class Statistika(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField()


class Statistika_text(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=7000)


class About_one(models.Model):
    image = models.ImageField(upload_to='midea/about/')
    title = models.CharField(max_length=256)
    text = models.TextField(max_length=7000)


class Aqili_gap(models.Model):
    full_name = models.CharField(max_length=256)
    job_nmae = models.CharField(max_length=256)
    text = models.TextField(max_length=150)
    image = models.ImageField(upload_to='midea/avatar/')


class Factory_about(models.Model):
    image = models.ImageField(upload_to='midea/team/')
    full_name = models.CharField(max_length=256)
    job_name = models.CharField(max_length=256)
    text = models.TextField(max_length=500)
    videofile= models.CharField(max_length=600, null=True)



class Logo(models.Model):
    images = models.ImageField(upload_to='midea/logo/')


class Category_certificat(models.Model):
    name = models.CharField(max_length=250)


class Certificats(models.Model):
    name = models.ForeignKey(Category_certificat, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='midea/certificat/')
