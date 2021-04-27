from django.views import View
from django.http import JsonResponse
from .models import Family
from django.core.serializers import serialize

class FamilyView(View):

    def get(self, request):
        families = Family.objects.all()
        serialize_families = serialize('python', families)

        data = {'families': serialize_families}
        return JsonResponse(data)

