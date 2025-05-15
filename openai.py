# Auto Chat Reply Example - Created by Hashir Adnan (THFNexus)
# This script analyzes a WhatsApp-style chat conversation and uses OpenAI to generate a funny or relevant response.

from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key="<Your OpenAI Key Here>",
)

# Simulated chat history (replace with dynamic input if needed)
chat_history = '''
[20:30, 12/6/2024] THFNexus: jo sunke coding ho sake?
[20:30, 12/6/2024] Tahseen: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Tahseen: ye
[20:30, 12/6/2024] Tahseen: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] THFNexus: This is hindi
[20:31, 12/6/2024] THFNexus: send me some english songs
[20:31, 12/6/2024] THFNexus: but wait
[20:31, 12/6/2024] THFNexus: this song is amazing
[20:31, 12/6/2024] THFNexus: so I will stick to it
[20:31, 12/6/2024] THFNexus: send me some english songs also
[20:31, 12/6/2024] Tahseen: hold on
[20:31, 12/6/2024] THFNexus: I know what you are about to send
[20:32, 12/6/2024] THFNexus: 😂😂
[20:32, 12/6/2024] Tahseen: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] THFNexus: okok
[20:33, 12/6/2024] Tahseen: Haan
'''

# Generate response from OpenAI
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a person named THFNexus who speaks both Hindi and English. "
                "You are an Indian coder with a sarcastic and funny tone. "
                "Your job is to analyze the conversation and respond like a witty friend. "
                "Avoid repeating names and timestamps."
            )
        },
        {"role": "user", "content": chat_history}
    ]
)

# Output the AI-generated response
print("\n🤖 Auto-Generated Response:")
print(completion.choices[0].message.content)
