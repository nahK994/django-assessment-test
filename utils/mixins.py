from rest_framework.response import Response
from rest_framework import status


class ModelManagerMixin:
    http_method_names = ["post", "get", "patch", "delete"]
    
    
    def get_validation_errors(self, serializer):
        errors = {}
        for field_name, field_errors in serializer.errors.items():
            errors[field_name] = ', '.join(field_errors)
        return errors


    def list(self, request):
        serialized_data = self.get_serializer(self.get_queryset(), many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        if not pk.isnumeric():
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        filtered_data = self.get_queryset().filter(pk=pk)
        if filtered_data:
            serializer = self.get_serializer(filtered_data[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)
    
    
    def create(self, request):
        request_data = request.data

        serialized_info = self.get_serializer(data=request_data)
        if serialized_info.is_valid():
            serialized_info.save()
            
            return Response(serialized_info.data, status=status.HTTP_201_CREATED)
        
        return Response(self.get_validation_errors(serialized_info), status=status.HTTP_400_BAD_REQUEST)
        

    def update(self, request, pk, *args, **kwargs):
        if not pk.isnumeric():
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
        
        filtered_info = self.get_queryset().filter(id=pk)
        if not filtered_info:
            return Response("No such item", status=status.HTTP_404_NOT_FOUND)
        
        serialized_info = self.get_serializer(filtered_info[0], data=request.data)
        if serialized_info.is_valid():
            serialized_info.save()

            return Response(serialized_info.data, status=status.HTTP_200_OK)
        
        return Response(self.get_validation_errors(serialized_info), status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk):
        if not pk.isnumeric():
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        filtered_info = self.get_queryset().filter(id=pk)
        if not filtered_info:
            return Response("No such item", status=status.HTTP_404_NOT_FOUND)
        filtered_info.delete()

        return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)
