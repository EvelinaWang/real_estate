from autogen import AssistantAgent
from config import llm_config

def create_retriever_agent():
    return AssistantAgent(
        name="RetrieverAgent",
        llm_config=llm_config,
        system_message="你是一个向量检索专家，负责从数据库中检索相关房产信息。",
        is_termination_msg=lambda x: isinstance(x, dict) and "TERMINATE" in str(x.get("content", "")).upper(),
    )
