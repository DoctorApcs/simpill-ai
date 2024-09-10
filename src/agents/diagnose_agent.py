from llama_index.agent.openai import OpenAIAgent
from src.agents.prompts import DOCTOR_AI_PROMPT
from src.agents.tools import retrieve_condition
from llama_index.core.tools import FunctionTool


class DiagnoseAgent:
    def __init__(self):
        self.agent = self._init_agent()
        print("Initialized diagnose agent")

    def _init_agent(self):
        agent = OpenAIAgent.from_tools(
            tools=self._init_tools(),
            system_prompt=DOCTOR_AI_PROMPT,
            verbose=True,
        )
        return agent

    def _init_tools(self):
        return [
            FunctionTool.from_defaults(
                fn=retrieve_condition, description="Retrieve condition from symptoms"
            )
        ]

    def run(self, diagnose_state: dict):

        return self.agent.chat(str(diagnose_state))
