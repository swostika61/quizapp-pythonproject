from django.urls import path

from quiz_app.views import QuizView


urlpatterns = [
    path('play-quiz/',QuizView.playQuiz,name='play-quiz'),
    path('select-topic/',QuizView.selectTopic,name='select-topic'),
]