class SerializerFactory:
    def __init__(self):
        self._creators = dict()

    def register_serializer(self, fmt, serializer):
        self._creators[fmt] = serializer

    def get_serializer(self, fmt):
        creator = self._creators.get(fmt)
        if not creator:
            raise ValueError(fmt)
        return creator()
