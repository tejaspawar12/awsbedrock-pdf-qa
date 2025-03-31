# bedrock_llm.py

import os
from dotenv import load_dotenv
import boto3
from langchain_community.chat_models import BedrockChat

load_dotenv()

def get_bedrock_llm():
    """
    Returns a BedrockChat LLM client using Claude 2.1
    """
    bedrock_client = boto3.client(
        "bedrock-runtime",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    # Claude 2.1 Model ID:
    llm = BedrockChat(
        client=bedrock_client,
        model_id="anthropic.claude-v2:1",  # 👈 Claude 2.1 Bedrock model ID
        model_kwargs={
            "temperature": 0.3,
            "top_k": 250,
            "top_p": 0.9,
            "max_tokens": 1024  # 👈 correct key is max_tokens (not max_gen_len)
        }
    )

    return llm
