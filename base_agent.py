from openai import OpenAI
import os

class BaseAgent:
    def __init__(self):
        self.client = OpenAI(
            base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        self.headers = {
            "HTTP-Referer": "https://travel-agent.com",
            "X-Title": "AI Travel Designer"
        }
        self.model = "anthropic/claude-3-haiku"  # Free and reliable model