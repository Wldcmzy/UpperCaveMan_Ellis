from pydantic import BaseSettings, Extra, Field


class QWeather(BaseSettings):
    code: int = Field(0,alias="CODE")
    city: str = Field(0,alias="CITY")

    class Config:
        extra = "allow"
        case_sensitive = False
        anystr_lower = True


class Time(BaseSettings):
    hour: int = Field(0,alias="HOUR")
    minute: int = Field(0,alias="MINUTE")

    class Config:
        extra = "allow"
        case_sensitive = False
        anystr_lower = True


class Config(BaseSettings):
    # plugin custom config
    plugin_setting: str = "default"
    weather_qq_friends: list[QWeather()] = []
    weather_qq_groups: list[QWeather()] = []
    weather_inform_time: list[Time()] = []

    class Config:
        extra = Extra.allow
        case_sensitive = False
