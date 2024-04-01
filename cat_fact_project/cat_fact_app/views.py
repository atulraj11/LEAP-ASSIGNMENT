from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .tasks import fetch_cat_facts_task
from .models import CatFact
from .serializers import CatFactSerializer

class HealthView(APIView):
    def get(self,request):
        return Response(status=200)

class FetchFact(APIView):
    def get(self, request):
        task_result = fetch_cat_facts_task.delay()
        task_success = task_result.get()
      
        if task_success:
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetFact(APIView):

    def get(self,request):
        try:
            cat_fact = CatFact.objects.all()
            if cat_fact:
                serializer = CatFactSerializer(cat_fact[0])
                first_text = serializer.data['fact']

                return Response({'Facts about Cat': first_text},status=status.HTTP_200_OK)
            else:
                return Response({'error': 'no_task_has_been_queued_yet'})
        except Exception as e:
            return Response({'error': str(e)})
