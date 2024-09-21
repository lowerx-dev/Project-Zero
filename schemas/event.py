from pydantic import BaseModel, Field

class EventSchema(BaseModel):

    eventName: str  = Field(default=...)
    eventData: dict = Field(default={})