from django.db import models
from django.db.models.fields import EmailField

class_opted_choices =(
    ('1','5'),
    ('2','6'),
    ('3','7'),
    ('4','8'),
    ('5','9'),
    ('6','10'),
)
class Student(models.Model):
    s_name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    DOB = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField()
    phone_no = models.BigIntegerField()
    email = models.EmailField()
    class_opted = models.CharField(max_length=20,
                                    choices=class_opted_choices,
                                    default='5'
                                )
    marks = models.FloatField()
    date_enrolled = models.DateField(auto_now=True)


    def uniqueEmail(self):
        if Student.objects.filter(email  = self.email):
            return True
        else:
            False     

    def uniquePhone(self):
        if Student.objects.filter(phone_no  = self.phone_no):
            return True
        else:
            False         



    

