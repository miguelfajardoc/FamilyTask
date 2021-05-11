from django.views import View
from django.http import JsonResponse
from .models import Family
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

@method_decorator(csrf_exempt, name='dispatch')
class FamilyView(View):

    def get(self, request):
        families = Family.objects.all()
        serialize_families = serialize('python', families)

        data = {'families': serialize_families}
        return JsonResponse(data, status=200)

    def post(self, request):
        body = json.loads(request.body)

        try:
            name = body.get('name')
            family = Family(
                name = name
            )
            family.save()
            data = {'message': f'new family created with id {family.id}'}
            status = 201
        except Exception as ex:
            data = {'message': f'missing parameters {ex}'}
            status = 400
        return JsonResponse(data, status=status)


@method_decorator(csrf_exempt, name='dispatch')
class FamilyUpdateDeleteView(View):

    def put(self, request, family_id):  # extra url parameter book_id is manadaotry
        family = Family.objects.get(id=family_id)

        put_body = json.loads(request.body)
        family.name = put_body.get('name')
        family.save()

        data = {
            'message': f'Name of the family {family_id} has been updated'
        }
        return JsonResponse(data)

    def delete(self, request, family_id):
        family = Family.objects.get(id=family_id)
        family.delete()
        data = {
            'message': f'Name of the family {family_id} has been deleted'
        }
        return JsonResponse(data)