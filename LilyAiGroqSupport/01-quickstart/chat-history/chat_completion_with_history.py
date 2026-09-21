from groq import Groq
import os

# GROQ_MODEL: Groq model to use for chat/text generation (set via environment variable, or edit here)
GROQ_MODEL = os.environ.get("GROQ_MODEL", "<your-groq-model-id>")


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    user_input = input("Chat with history: ")

    messages.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=GROQ_MODEL,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )


    assistant_response = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})

    print(assistant_response + "\n")