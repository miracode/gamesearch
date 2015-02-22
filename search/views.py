from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import GameSearchForm
from django.views.generic.edit import FormView
from api_queries import get_games_list, get_game_details
from rest_framework import generics, views
from .models import Game
from serializers import GameSerializer

from rest_framework.response import Response

from copy import copy


def index(request):
    if request.method == "POST":
        form = GameSearchForm(request.POST)
        if form.is_valid():
            print form
            return HttpResponseRedirect('/results/')
    else:
        form = GameSearchForm()

    return render(request, 'search/index.html', {'form': form})


def results(request):
    context = request.POST

    games_xml = get_games_list(request.POST['title'], request.POST['platform'])

    # print dir(request.session)
    # print request.session.iteritems()

    return render(request, 'search/results.html',
                 {'results': games_xml, 'context': context},
                 # content_type="application/xhtml+xml",
                 )


def api(request):

    return render(request, 'search/api.html')


class GameView(views.APIView):

    def get(self, request):
        """
        Get response from API
        """
        # get list of dictionaries of games

        name = self.request.QUERY_PARAMS.get('name', None)

        game_id = self.request.QUERY_PARAMS.get('game_id', None)

        result = get_game_details(name=name, game_id=game_id)

        # result = get_game_details(result)

        game_serializer = GameSerializer(data=result, many=True)

        if game_serializer.is_valid():
            return Response(game_serializer.data, status=200)

        else:
            return Response(game_serializer.errors, status=400)

    def post(self, request):
        """
        Give information that needs to be saved
        """

        # nothing currently being saved.
        request_data = copy(request.DATA)

        print request_data
        game_serializer = GameSerializer(data=request_data)

        if game_serializer.is_valid():
            print game_serializer.data
            return Response(game_serializer.data, status=200)

        else:
            return Response(game_serializer.errors, status=400)

# class GameView(generics.ListAPIView):

#     model = Game
#     serializer_class = GameSerializer

#     def get_queryset(self):
#         return Game.objects.all()


# class GameSearchView(FormView):
#     template_name = 'search/index.html'
#     form_class = GameSearchForm
#     success_url = '/results/'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             return render(request, success_url)
