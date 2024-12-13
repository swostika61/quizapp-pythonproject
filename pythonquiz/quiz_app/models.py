from djongo import models

class Questions(models.Model):
    topic = models.CharField(max_length=200, default="")
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
    
class UserResult(models.Model):
    username = models.CharField(max_length=200)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class QuizTopics(models.Model):
    topic = models.CharField(max_length=200)
    

    # def __str__(self):
    #     return self.question_text
