import datetime
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets
from .models import CNAB
from .serializers import CNABSerializer

from rest_framework import views
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import status


class CNABViewSet(viewsets.ModelViewSet):
    queryset = CNAB.objects.all()
    serializer_class = CNABSerializer

   
def process_cnab_file(file):    
    file_content = file.read().decode()

    lines = file_content.split('\n')

    for line in lines:
        if line:
            transaction_type = line[0]
            occurrence_date = line[1:9]
            value = line[9:18]
            cpf = line[19:29]
            card = line[30:41]
            occurrence_hour = line[42:47]
            owner_name = line[48:61]
            store_name = line[62:80]

            occurrence_date = datetime.datetime.strptime(occurrence_date, '%Y%m%d')
            occurrence_hour = datetime.datetime.strptime(occurrence_hour, '%H%M%S').time()

            value = Decimal(value) / Decimal(100)

            cnab = CNAB(transaction_type=transaction_type, occurrence_date=occurrence_date, value=value, cpf=cpf, card=card, occurrence_hour=occurrence_hour, owner_name=owner_name, store_name=store_name)
            cnab.save()

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if not file.name.endswith('.cnab'):
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, content='O arquivo deve ser um arquivo CNAB válido.')
        process_cnab_file(file) 
        return HttpResponse(status=status.HTTP_200_OK, content='Arquivo processado com sucesso')
    else:
        return render(request, 'upload.html')

class CNABImportView(views.APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        file = request.data['file']
        process_cnab_file(file)
        return Response({'status': 'ok'})


class CNABListView(views.APIView):
    def get(self, request):
        cnabs = CNAB.objects.all()
        store_balances = cnabs.values('store_name').annotate(balance=Sum('value'))
        return Response(store_balances)