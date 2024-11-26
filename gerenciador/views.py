from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projetos
from .serializers import ProjetosSerializer

# Create your views here.

class ProjetosAPIView(APIView):
  def get(self, request):
    projects = Projetos.objects.all() #recuperar todos os campos do banco
    serializer = ProjetosSerializer(projects, many=True) #serializar a lista de objetos
    return Response(serializer.data) #retorna como JSON
