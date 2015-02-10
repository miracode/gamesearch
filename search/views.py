from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import GameSearchForm
from django.views.generic.edit import FormView
from .forms import GameSearchForm
from api_queries import get_games_list


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
