from django.shortcuts import render

# Create your views here.
from django.views import View


class NovoJc(View):
    def get(self, request):
        # pais = {
        #    'countries': Country.objects.all()
        # }
        return render(request, 'modelos.html', context=None)
