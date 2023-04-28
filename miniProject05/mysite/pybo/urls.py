from django.urls import path

from .views import base_views, question_views, answer_views, market_views, Premier_League, LaLiga, Bundesliga, SeriaA, League1, KLeague1

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),

    # market_views.py
    path('Premier_League/', Premier_League.player_list, name='premier_league_list'),
    path('LaLiga/', LaLiga.player_list, name='laliga_list'),
    path('Bundesliga/', Bundesliga.player_list, name='bundesliga_list'),
    path('SeriaA/', SeriaA.player_list, name='seria_a_list'),
    path('League1/', League1.player_list, name='league1_list'),
    path('KLeague1/', KLeague1.player_list, name='kleague1_list')

]