from autogen import UserProxyAgent
from config import llm_config

def create_user_agent():
    return UserProxyAgent(
        name="UserAgent",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: isinstance(x, dict) and "TERMINATE" in str(x.get("content", "")).upper(),
        code_execution_config=False,
        default_auto_reply="TERMINATE if you're done.",
        description="客户提问者，提出房产相关问题。",
    )
