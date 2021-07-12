import json
import xml.etree.ElementTree as et
from serializer_factory import SerializerFactory


def test():
    pass


class JSONSerializer:
    def __init__(self):
        self.object = dict()

    def start_object(self, object_name, object_id):
        self.object['id'] = object_id

    def add_property(self, name, value):
        self.object[name] = value

    def to_str(self):
        return json.dumps(self.object)


class XMLSerializer:
    def __init__(self):
        self.element = None

    def start_object(self, object_name, object_id):
        self.element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        c_element = et.SubElement(self.element, name)
        c_element.text = value

    def to_str(self):
        return et.tostring(self.element, encoding='unicode')


factory =  SerializerFactory()
factory.register_serializer('JSON', JSONSerializer)
factory.register_serializer('XML', XMLSerializer)


class ObjectSerializer:
    def serialize(self, serializable, fmt):
        serializer = factory.get_serializer(fmt)
        serializable.serialize(serializer)
        return serializer.to_str()