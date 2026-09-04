# FAQ Chatbot

## 📌 About the Project

This is a simple FAQ Chatbot built using Python. It allows users to ask questions about topics such as Python, Artificial Intelligence, Machine Learning, NLP, and programming.

The chatbot uses Natural Language Processing techniques to find the FAQ question that is most similar to the user's question and provides the related answer.

##  Features

- Simple and user-friendly graphical interface
- Answers frequently asked questions
- Uses text similarity to understand user questions
- Provides a response when a matching FAQ is found
- Shows a helpful message when it does not know the answer
- Press Enter to send a question

## Technologies Used

- Python
- Tkinter
- JSON
- Scikit-learn
- TF-IDF
- Cosine Similarity

## How It Works

The chatbot stores questions and answers in a JSON file.

When the user enters a question, the chatbot:

1. Converts the FAQ questions into numerical representations using TF-IDF.
2. Converts the user's question in the same way.
3. Compares the user's question with the stored FAQ questions using cosine similarity.
4. Finds the most similar question.
5. Displays the corresponding answer.

## Project Files

- `app.py` — Main chatbot application
- `faqs.json` — Contains FAQ questions and answers
- `requirements.txt` — Required Python library
- `.gitignore` — Files ignored by Git

## Installation

Install the required library using:

```bash
pip install -r requirements.txt

▶️ How to Run:

Run the chatbot with:
python app.py

A chatbot window will open. Type your question in the input box and press Send or press Enter.

 Purpose

This project was created as part of my CodeAlpha internship tasks to practice Python programming, GUI development, JSON data handling, and basic Natural Language Processing techniques.