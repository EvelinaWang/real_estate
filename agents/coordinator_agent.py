from autogen import AssistantAgent
from config import llm_config

def create_coordinator_agent():
    return AssistantAgent(
        name="CoordinatorAgent",
        llm_config=llm_config,
        system_message=(
            "你是房地产智能体协调者，负责在Retriever、Researcher、Responder之间传递信息，"
            "保证协作流程顺利进行，并向User代理反馈最终结果。"
        ),
        is_termination_msg=lambda x: isinstance(x, dict) and "TERMINATE" in str(x.get("content", "")).upper(),
    )
