from typing import Dict, Optional
from pydantic import BaseModel, Field


class ActionSchema(BaseModel):
    """
    Schema for validation when "sending" an action. This format is expected by the
    "_send" method of the Operator class.
    """

    # fully qualified name of the receiving operator.
    # if not specified the action is sent to all operators _but_ the sender
    to: Optional[str] = Field(None)

    # natural language explanation for the action
    thoughts: str

    # the action name
    action: str

    # the action arguments
    args: Dict


class MessageSchema(ActionSchema):
    """
    Schema for validation of a received message. This format is expected by the
    "_receive" method of the Operator class.
    """
    # the sending operator
    from_field: str = Field(..., alias='from')
