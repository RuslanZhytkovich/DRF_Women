import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women





class WomenSerializer(serializers.ModelSerializer):         # в этом классе пишем такие же поля как и в модели
    class Meta:
        model = Women
        fields = ("title", "content", "cat",)









def decode():  # из JSON в словарь
    stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
    data = JSONParser.parse(stream)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)