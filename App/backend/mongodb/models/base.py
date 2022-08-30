from bson import ObjectId


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
