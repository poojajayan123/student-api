from djongo import models
# Create your models here.

class polls(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    

    def __str__(self):
        return self.question_text

    class Meta:
        db_table  = 'polls'



class choice(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    question = models.ArrayReferenceField(to=polls)
    choice_text = models.CharField(max_length = 20)
    votes = models.IntegerField(default=0)



    def __str__(self):
        return self.choice_text

    class Meta:
        db_table= "choice"

