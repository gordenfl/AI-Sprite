import openai
import os
from dotenv import load_dotenv
load_dotenv()

# 设置 API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat():
    print("Chatbot is running! Type 'exit' to stop.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        bot_reply = response['choices'][0]['message']['content']
        print("Bot:", bot_reply)
        messages.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    chat()
