from unicodedata import name
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """ serialize a name field for testing api view """
    name = serializers.CharField(max_length=10)
     