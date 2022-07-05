from pydantic import BaseModel, Extra

class Config(BaseModel, extra=Extra.ignore):
    noise_qq_friends: list[str] = []
    noise_qq_groups: list[str] = []