# Auto-Reply Bot - Created by Hashir Adnan
# Description:
# This Python script automatically detects messages in a WhatsApp web-like interface
# and responds using OpenAI based on context. Designed for fun roasting responses.
# Libraries Used: pyautogui, pyperclip, time, openai

import pyautogui
import time
import pyperclip
from openai import OpenAI

# --- Configuration ---
API_KEY = "<Your OpenAI Key Here>"
SENDER_NAME = "Rohan Das"  # Name to detect the last message sender

# Screen coordinates (adjust based on your screen resolution)
CHROME_ICON_COORDS = (1639, 1412)
TEXT_AREA_START = (972, 202)
TEXT_AREA_END = (2213, 1278)
WHATSAPP_CLICK = (1994, 281)
TEXT_INPUT_BOX = (1808, 1328)

# --- Initialize OpenAI Client ---
client = OpenAI(api_key=API_KEY)

# --- Helper Functions ---

def is_last_message_from_sender(chat_log: str, sender_name=SENDER_NAME) -> bool:
    """Check if the last message in chat history is from the given sender."""
    last_segment = chat_log.strip().split("/2024] ")[-1]
    return sender_name in last_segment

def generate_reply(chat_history: str) -> str:
    """Generate a funny roast reply using OpenAI."""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Naruto who speaks Hindi + English. You are from India and a coder. You analyze chat history and roast people in a funny way."},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das:"},
            {"role": "user", "content": chat_history}
        ]
    )
    return completion.choices[0].message.content

# --- Main Bot Loop ---

def run_bot():
    print("Starting Auto-Reply Bot...")

    # Click on Chrome to activate
    pyautogui.click(*CHROME_ICON_COORDS)
    time.sleep(1)

    while True:
        try:
            time.sleep(5)

            # Select chat area
            pyautogui.moveTo(*TEXT_AREA_START)
            pyautogui.dragTo(*TEXT_AREA_END, duration=2.0, button='left')

            # Copy selected text
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)

            # Click to focus chat
            pyautogui.click(*WHATSAPP_CLICK)

            chat_history = pyperclip.paste()
            print("Chat History Copied:")
            print(chat_history)

            if is_last_message_from_sender(chat_history):
                response = generate_reply(chat_history)
                pyperclip.copy(response)

                # Paste and send reply
                pyautogui.click(*TEXT_INPUT_BOX)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
                pyautogui.press('enter')

                print("Reply sent:", response)

        except Exception as e:
            print(f"[Error] {e}")
            time.sleep(5)

# --- Run ---
if __name__ == "__main__":
    run_bot()
