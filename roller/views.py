from django.views.generic import ListView, DetailView, TemplateView, View
from django.http import HttpResponse
from roller.models import Table, RandomPick
import random

class HomeView(TemplateView):
    template_name = "roller/home.html"


class TableListView(ListView):
	model = Table
	template_name = "roller/table_list.html"


class TableView(DetailView):
	model = Table
	context_object_name = 'table'
	template_name = "roller/table.html"


class RollView(View):
	def get(self, request):
		table_id = request.GET['Table']
		table = Table.objects.get(pk=table_id)

		rollValue = random.randint(1,100)
		rPicks = table.randompick_set.filter(start_value__lte=rollValue, end_value__gte=rollValue)
		rPick = rPicks[0]

		return HttpResponse("Value roller: %s , got %s:%s,%s RandomPick" % (rollValue,
			rPick.text, rPick.start_value, rPick.end_value))
