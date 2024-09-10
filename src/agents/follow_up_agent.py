from llama_index.llms.openai import OpenAI
from .prompts import FOLLOW_UP_PROMPT, REVIEW_PROMPT
import json


class FollowUpAgent:

    def ask_follow_up_question(self, diagnose_state: dict):
        llm = OpenAI(model="gpt-4o-mini")
        prompt = FOLLOW_UP_PROMPT.format(diagnose_state=diagnose_state)
        response = llm.complete(prompt, response_format={"type": "json_object"})
        response_json = json.loads(response.text)
        return {"follow_up_question": response_json["follow_up_question"]}

    def review_human_input(self, diagnose_state: dict):
        llm = OpenAI(model="gpt-4o-mini")
        prompt = REVIEW_PROMPT.format(diagnose_state=diagnose_state)
        response = llm.complete(prompt, response_format={"type": "json_object"})
        response_json = json.loads(response.text)
        return {"agent_response": response_json["agent_response"]}
