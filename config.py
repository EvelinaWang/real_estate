import os
from dotenv import load_dotenv

load_dotenv()

llm_config = {
    "config_list": [{"model": "gpt-3.5-turbo", "api_key": os.environ["OPENAI_API_KEY"]}],
}
