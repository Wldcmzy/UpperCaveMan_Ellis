from pydantic import BaseModel, Extra

class Config(BaseModel, extra=Extra.ignore):
    repeat_judger_group: list[str] = []
    repeat_judger_group_interrupt: list[str] = []
    repeat_judger_threshold: int = 3
    repeat_judge_threshold_random_add: int = 0