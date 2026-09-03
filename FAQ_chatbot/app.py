import tkinter as tk
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load FAQ data
with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Get FAQ questions
questions = [faq["question"] for faq in faqs]

# Convert questions into numbers
vectorizer = TfidfVectorizer(stop_words="english")
faq_vectors = vectorizer.fit_transform(questions)


# Find the best answer
def get_answer(question):
    user_vector = vectorizer.transform([question])

    scores = cosine_similarity(user_vector, faq_vectors)
    best_match = scores.argmax()

    if scores[0][best_match] < 0.2:
        return "Sorry, I don't know the answer to that."

    return faqs[best_match]["answer"]


# Send message
def send_message():
    question = input_box.get().strip()

    if question:
        chat.insert(tk.END, "You: " + question + "\n")

        answer = get_answer(question)
        chat.insert(tk.END, "Bot: " + answer + "\n\n")

        input_box.delete(0, tk.END)


# Create window
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("600x500")


# Title
title = tk.Label(
    root,
    text=" FAQ Chatbot ",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)


# Chat area
chat = tk.Text(
    root,
    height=18,
    width=65,
    font=("Arial", 11),
    wrap=tk.WORD
)
chat.pack(padx=20)


# Input area
input_box = tk.Entry(
    root,
    width=45,
    font=("Arial", 12)
)
input_box.pack(side=tk.LEFT, padx=(40, 10), pady=15)


# Send button
send_button = tk.Button(
    root,
    text="Send",
    font=("Arial", 11, "bold"),
    command=send_message
)
send_button.pack(side=tk.LEFT)


# Welcome message
chat.insert(
    tk.END,
    "Bot: Hello! Ask me something about Python, AI, or programming.\n\n"
)


# Press Enter to send
root.bind("<Return>", lambda event: send_message())


# Start the application
root.mainloop()