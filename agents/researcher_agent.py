from autogen import AssistantAgent
from config import llm_config

def create_researcher_agent():
    return AssistantAgent(
        name="ResearcherAgent",
        llm_config=llm_config,
        system_message=(
            "你是房地产研究专家，根据Retriever提供的信息，分析房源的优劣势、城市背景、房价走势等，"
            "为Responder提供更丰富的回答内容支持。"
        ),
        is_termination_msg=lambda x: isinstance(x, dict) and "TERMINATE" in str(x.get("content", "")).upper(),
    )

