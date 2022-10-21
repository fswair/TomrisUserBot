from inspect import signature
from pydantic.dataclasses import dataclass
from pydantic import BaseModel
from submodules.MentoDB import PrimaryKey, UniqueMatch


@dataclass
class TomrisConfigModel(BaseModel):
    name: PrimaryKey(str)
    author: str

    unique_match: UniqueMatch("name", "author")
