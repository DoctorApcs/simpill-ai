from typing import TypedDict, List, Annotated, Optional
import operator


class DiagnosisState(TypedDict):
    query: str
    follow_up_question: Optional[str]
    human_response: Optional[str]
    follow_up_question: Optional[str]
    agent_response: Optional[str]
