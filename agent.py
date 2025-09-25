import os
from slack_bolt import App
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

slack_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Escutar mensagens em canais
@slack_app.message("")
def handle_message(event, say):
    user_message = event["text"]

    # Chamar ChatGPT
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}]
    )

    ai_reply = response.choices[0].message.content

    # Responder no Slack
    say(ai_reply)

if __name__ == "__main__":
    slack_app.start(port=int(os.environ.get("PORT", 3000)))
