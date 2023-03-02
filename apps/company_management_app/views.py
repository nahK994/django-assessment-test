from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer
from .models import Company
from rest_framework import viewsets


class CompanyTypeViewset(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    http_method_names = ["post", "get", "patch", "delete"]

    def list(self, request):
        serialized_comapny = self.get_serializer(self.get_queryset(), many=True)
        return Response(serialized_comapny.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        if not pk.isnumeric():
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        filtered_company = self.get_queryset().filter(pk=pk)
        if filtered_company:
            serializer = self.get_serializer(filtered_company[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

    
    def create(self, request):
        company = request.data
        
        serialized_comapny = self.get_serializer(data=company)
        if serialized_comapny.is_valid():
            serialized_comapny.save()
            return Response(serialized_comapny.data, status=status.HTTP_201_CREATED)
            
        return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
        

    def update(self, request, pk, *args, **kwargs):
        if not pk.isnumeric():
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
        
        filtered_company = self.get_queryset().filter(id=pk)
        if not filtered_company:
            return Response("No such company", status=status.HTTP_404_NOT_FOUND)
        
        serialized_comapny = self.get_serializer(filtered_company[0], data=request.data)
        if serialized_comapny.is_valid():
            serialized_comapny.save()
            return Response(serialized_comapny.data, status=status.HTTP_200_OK)
        
        return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk):
        if not pk.isnumeric():
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        filtered_company = self.get_queryset().filter(id=pk)
        if not filtered_company:
            return Response("No such company", status=status.HTTP_404_NOT_FOUND)
        filtered_company.delete()
        return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)
