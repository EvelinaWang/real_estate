from autogen import AssistantAgent
from config import llm_config

def create_responder_agent():
    return AssistantAgent(
        name="ResponderAgent",
        llm_config=llm_config,
        system_message=(
            "你是房地产客服，负责将Researcher提供的分析结果转换为清晰、自然、亲切的回复给客户，"
            "可以结合房源细节做推荐，注意避免术语堆砌。"
        ),
        is_termination_msg=lambda x: isinstance(x, dict) and "TERMINATE" in str(x.get("content", "")).upper(),
    )

# from autogen import ConversableAgent
# from config import llm_config

# def create_responder_agent():
#     return ConversableAgent(
#         name="ResponderAgent",
#         llm_config=llm_config,
#         system_message="你是一个房地产客服 AI 助手，请根据 RetrieverAgent 提供的房源信息，生成自然、有帮助的回复，不要重复或兜圈子。回答完一次后即可结束任务。",
#         human_input_mode="NEVER",
#         is_termination_msg=lambda msg: msg.get("name") == "ResponderAgent",
#         code_execution_config={"use_docker": False},
#     )
