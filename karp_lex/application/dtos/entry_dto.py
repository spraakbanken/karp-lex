from datetime import datetime
from typing import TypeVar, Generic, Optional
import uuid

from pydantic.generics import GenericModel


T = TypeVar("T")


def to_lower_camel(s: str) -> str:
    return "".join(
        word.capitalize() if i > 0 else word for i, word in enumerate(s.split("_"))
    )


class EntryDto(GenericModel, Generic[T]):
    entry: T
    last_modified_by: str
    last_modified: datetime
    entity_id: Optional[uuid.UUID]
    message: str
    entry_id: Optional[str]
    version: Optional[int]
    discarded: bool = False

    class Config:
        extra = "forbid"
        alias_generator = to_lower_camel
