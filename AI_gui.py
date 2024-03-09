import requests
import api_key
import guesser_gui_OS
import calculator_OS
import greetings_OS
import goodbyes_OS
import keywords_OS
import responses_OS
import random
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from calculator_OS import run_calculator
import threading
import subprocess

greetings = greetings_OS.greetings_data
goodbyes = goodbyes_OS.goodbyes_data
keywords = keywords_OS.keywords_data
responses = responses_OS.responses_data

API_KEY = api_key.api_key_data

conversation_history = []

def generate_chatgpt_response(input_text):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "prompt": input_text,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        response_data = response.json()
        chatgpt_response = response_data["choices"][0]["text"].strip() if "choices" in response_data else ""
        return chatgpt_response
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return ""

def show_conversation_history():
    history_window = tk.Toplevel(root)
    history_window.title("Conversation History")

    history_text = tk.Text(history_window, wrap="word", font=("Arial", 12))
    history_text.pack(expand=True, fill="both")

    for speaker, text in conversation_history:
        history_text.insert(tk.END, f"{speaker}: {text}\n")

    history_text.config(state=tk.DISABLED)

def handle_user_input():
    user_input = user_entry.get().lower()
    user_entry.delete(0, tk.END)

    conversation_history.append(("You", user_input))

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    chat_box.see(tk.END)

    if user_input == "game" or user_input == "games":
        chat_box.insert(tk.END, "Sonic AI: Game launched! Enjoy playing!\n")
        chat_box.config(state=tk.DISABLED)

        if user_input == "game":
            subprocess.Popen(['gusser_gui_OS.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.Popen(['gusser_gui_OS.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Sonic AI: What else can I do for you?\n")
        chat_box.see(tk.END)
        return

    elif user_input in greetings:
        chat_box.insert(tk.END, "Sonic AI: " + random.choice(greetings) + "\n")
        chat_box.insert(tk.END, "Sonic AI: What can I do for you?\n")
    elif user_input == "bye" or user_input == "nothing":
        chat_box.insert(tk.END, "Sonic AI: " + random.choice(goodbyes) + "\n")
        user_entry.config(state=tk.DISABLED, bg="gray")
    elif user_input == "calculator":
        chat_box.insert(tk.END,
                        "Sonic AI: Sure, here's the calculator app (We are working on an inbuilt calculator too.)\n")
        chat_box.config(state=tk.DISABLED)
        run_calculator()
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Sonic AI: What else can I do for you?\n")
    else:
        keyword_found = False

        for index in range(len(keywords)):
            if keywords[index] in user_input:
                chat_box.insert(tk.END, "Sonic AI: " + responses[index] + "\n")
                keyword_found = True
                break

        if not keyword_found:
            chatgpt_response = generate_chatgpt_response(user_input)
            if chatgpt_response:
                chat_box.insert(tk.END, "Sonic AI: " + chatgpt_response + "\n")
            else:
                chat_box.insert(tk.END, "Sonic AI: Sorry, I can't help with that.\n")
            chat_box.insert(tk.END, "Sonic AI: What else can I do for you?\n")

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

def on_focus_in(event):
    if user_entry.get() == "Enter your response here":
        user_entry.delete(0, tk.END)
        user_entry.config(fg="black")

def on_focus_out(event):
    if user_entry.get() == "":
        user_entry.insert(0, "Enter your response here")
        user_entry.config(fg="gray")

def process_user_input(event=None):
    threading.Thread(target=handle_user_input).start()

def run_game():
    # Your game logic here
    pass

root = tk.Tk()
root.title("Sonic AI")
root.geometry("600x400")
root.configure(bg="deep sky blue")

style = ThemedStyle(root)
style.set_theme("equilux")

chat_frame = ttk.Frame(root, padding=10, relief="sunken", borderwidth=2)
chat_frame.grid(row=0, column=0, sticky="nsew")

chat_box = tk.Text(chat_frame, wrap="word", state=tk.DISABLED, font=("Arial", 13), bg="lightblue")
chat_box.pack(expand=True, fill="both")

user_entry = tk.Entry(root, font=("Arial", 13), fg="gray")
user_entry.grid(row=1, column=0, sticky="ew")
user_entry.insert(0, "Enter your response here")
user_entry.bind("<FocusIn>", on_focus_in)
user_entry.bind("<FocusOut>", on_focus_out)
user_entry.bind("<Return>", process_user_input)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
chat_box.config(state=tk.NORMAL)
chat_box.insert(tk.END, "Sonic AI: " + random.choice(greetings) + "\n")
chat_box.insert(tk.END, "Sonic AI: What can I do for you?\n")
chat_box.config(state=tk.DISABLED)

history_button = tk.Button(root, text="Show Conversation History", command=show_conversation_history)
history_button.grid(row=2, column=0, sticky="ew")

root.mainloop()

#Code is still a work in progress and not yet finished and is meant to be a simple representation of an "AI"
