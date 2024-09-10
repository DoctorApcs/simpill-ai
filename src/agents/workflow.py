from langgraph.graph import END, START, StateGraph
from src.agents.state import DiagnosisState
from src.agents.follow_up_agent import FollowUpAgent
from src.agents.diagnose_agent import DiagnoseAgent
from src.agents.human_agent import HumanInputAgent
import dotenv

dotenv.load_dotenv()


class WorkflowAgent:
    def __init__(self):
        workflow = StateGraph(state_schema=DiagnosisState)
        follow_up_agent = FollowUpAgent()
        diagnose_agent = DiagnoseAgent()
        human_input_agent = HumanInputAgent()

        workflow.add_node(
            "ask_follow_up_question", follow_up_agent.ask_follow_up_question
        )

        workflow.add_node("need_more_questions", follow_up_agent.review_human_input)
        workflow.add_node("diagnose", diagnose_agent.run)
        workflow.add_node("human_input", human_input_agent.run)

        workflow.add_edge(START, "ask_follow_up_question")
        workflow.add_edge("ask_follow_up_question", "human_input")
        workflow.add_edge("human_input", "need_more_questions")

        workflow.add_conditional_edges(
            "need_more_questions",
            (lambda review: "no" if review["agent_response"] == "no" else "yes"),
            {
                "yes": "ask_follow_up_question",
                "no": "diagnose",
            },
        )
        workflow.add_edge("diagnose", END)

        self.workflow = workflow

    async def run(self, diagnose_state: DiagnosisState):
        doctor_workflow = self.workflow.compile()
        return await doctor_workflow.ainvoke(diagnose_state)
