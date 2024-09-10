from src.agents.workflow import WorkflowAgent
from src.agents.state import DiagnosisState
import asyncio

query = DiagnosisState(query="I have a headache")
workflow = WorkflowAgent()
asyncio.run(workflow.run(query))
