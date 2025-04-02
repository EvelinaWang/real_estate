from autogen import GroupChat, GroupChatManager
from agents.user_agent import create_user_agent
from agents.retriever_agent import create_retriever_agent
from agents.researcher_agent import create_researcher_agent
from agents.responder_agent import create_responder_agent
from agents.coordinator_agent import create_coordinator_agent
from config import llm_config

def main():
    user_agent = create_user_agent()
    retriever = create_retriever_agent()
    researcher = create_researcher_agent()
    responder = create_responder_agent()
    coordinator = create_coordinator_agent()

    groupchat = GroupChat(
        agents=[retriever, researcher, responder, coordinator],
        messages=[],
        max_round=10,
        speaker_selection_method="round_robin",
    )

    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)
    user_agent.initiate_chat(manager, message="我想找一套位于阿拉巴马州的三室两卫房子，价格不超过30万美元")

if __name__ == "__main__":
    main()
