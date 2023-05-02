from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """
     A model class is the pythonic representation of a database table. This is a super class which every model will inherit.
     For instance, all table tables will have an id field.
    """
    id: Any
    __name__: str

    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()