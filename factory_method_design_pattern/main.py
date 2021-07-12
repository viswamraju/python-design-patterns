import song
import serializers


s1 = song.Song("1", 'title1', 'artist1')
serializer = serializers.ObjectSerializer()
print(serializer.serialize(s1, 'XML'))

