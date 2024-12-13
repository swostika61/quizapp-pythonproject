from django.forms import model_to_dict
from django.shortcuts import redirect, render

from quiz_app.models import Questions, QuizTopics, UserResult
from random import sample
from django.contrib.auth.decorators import login_required, user_passes_test
import json

# Create your views here.
class QuizView:
    
    def home(request):
        return render(request,"index.html")
    
    
    
    @login_required
    def dashboard(request):
        all_results = UserResult.objects.filter(username=request.user)
        # print(all_results[0].date)
        all_results_dict = []
        for result in all_results:
           all_results_dict.append({
                "score": result.score,
                "date": result.date,
           })

      
        return render(request, "dashboard.html", {
            "scores": all_results_dict[::-1],
            "average_score": round(sum([result['score'] for result in all_results_dict]) / len(all_results_dict), 2) if len(all_results_dict) > 0 else 0,
            "highest_score": round(max([result['score'] for result in all_results_dict]), 2) if len(all_results_dict) > 0 else 0,
            "lowest_score": round(min([result['score'] for result in all_results_dict]), 2) if len(all_results_dict) > 0 else 0,
            "total_attempts": len(all_results_dict)
        })
        
    @login_required
    def selectTopic(request):
        all_topics = list(QuizTopics.objects.all())
        json_topics = [model_to_dict(topic) for topic in all_topics]
        return render(request, "select_topic.html", {"topics": json_topics})
    

        
        
    @login_required
    def playQuiz(request):
        topic = request.GET.get('topic')
        is_retake = request.POST.get('is_retake', 'false') == 'true'
        
        
        if request.method == "POST":
            UserResult.objects.create(username=str(request.user), score=int(request.POST["score"]))
            if is_retake :
                return redirect("select-topic")
            
            return redirect("dashboard")
        else:  
            
            all_questions = list(Questions.objects.filter(topic=topic))
            random_questions = sample(all_questions, min(len(all_questions), 5))
            random_questions = [model_to_dict(question) for question in random_questions]

            return render(
                request, "play_quiz.html", {"quizzes_list": random_questions}
            )
        
        


class QuizPlayer:
    def restricted_access(request):
        return render(request,'index.html')
    