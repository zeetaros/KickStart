import re
from bson import ObjectId
from pydantic import BaseModel


def snake_to_camel_case(string: str) -> str:
    _string = str(string)
    if _string.isnumeric():
        return string
    tokens = _string.split("_")
    return tokens[0].lower() + "".join(t.title() for t in tokens[1:])


def camel_to_snake_case(string: str) -> str:
    _string = str(string)
    if _string.isnumeric():
        return string
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", string).lower()


class ObjectIdStr(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> ObjectId:
        if isinstance(v, (ObjectId, cls)):
            return v
        if isinstance(v, str) and ObjectId.is_valid(v):
            return ObjectId(v)
        raise ValueError("Not a valid ObjectId")


class ModBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        use_enum_values = True
        alias_generator = snake_to_camel_case
        json_encoders = {
            ObjectId: str,
            ObjectIdStr: str,
        }
