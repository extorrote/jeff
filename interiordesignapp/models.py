from django.db import models

class PostIndex(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    image1=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image2=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image3=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image4=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image5=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image6=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image7=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image8=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
    
class PostProject(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    image1=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image2=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image3=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image4=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image5=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image6=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image7=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    image8=models.ImageField(upload_to="images/post_index", blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title or "Untitled Project" #SI NO EXISTE EL CAMPO QUE PONGA AQUI ME VA VOTAR ERROR 
    
    



from django.db import models

class JobOpening(models.Model):
    DEPARTMENT_CHOICES = [
        ('furniture_design', 'Furniture Design'),
        ('interior_design', 'Interior Design'),
        ('property_management', 'Property Management'),
        ('property_remodeling', 'Property Remodeling'),
    ]

    title = models.CharField(max_length=100)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    employment_type = models.CharField(max_length=50, choices=[
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ])
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
