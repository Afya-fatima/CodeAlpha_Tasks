import tkinter as tk
from tkinter import ttk
import requests

API_URL = "http://localhost:5000/translate"


#window
root = tk.Tk()
root.title("Language Translator")
root.geometry("750x650")
root.resizable(False, False)
root.configure(bg="#f4f7fb")


#style
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TCombobox",
    font=("Arial", 11),
    padding=5
)

 #TITLE 

title = tk.Label(
    root,
    text=" Language Translator ",
    font=("Arial", 24, "bold"),
    bg="#f4f7fb",
    fg="#1f3c88"
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Translate text quickly and easily",
    font=("Arial", 11),
    bg="#f4f7fb",
    fg="#666666"
)
subtitle.pack(pady=(0, 20))

#  LANGUAGE SELECTION 

language_frame = tk.Frame(
    root,
    bg="#ffffff",
    padx=20,
    pady=15
)
language_frame.pack(padx=40, fill="x")

languages = [
    "English",
    "Urdu",
    "Arabic",
    "Turkish",
    "Hindi",
    "French",
    "Spanish",
    "German"
]

tk.Label(
    language_frame,
    text="From",
    font=("Arial", 11, "bold"),
    bg="#ffffff",
    fg="#333333"
).grid(row=0, column=0, padx=10)

source_language = ttk.Combobox(
    language_frame,
    values=languages,
    state="readonly",
    width=15
)
source_language.set("English")
source_language.grid(row=0, column=1, padx=10)

tk.Label(
    language_frame,
    text="To",
    font=("Arial", 11, "bold"),
    bg="#ffffff",
    fg="#333333"
).grid(row=0, column=2, padx=10)

target_language = ttk.Combobox(
    language_frame,
    values=languages,
    state="readonly",
    width=15
)
target_language.set("Urdu")
target_language.grid(row=0, column=3, padx=10)

#  INPUT 

tk.Label(
    root,
    text="Enter text",
    font=("Arial", 12, "bold"),
    bg="#f4f7fb",
    fg="#333333"
).pack(anchor="w", padx=50, pady=(20, 7))

input_text = tk.Text(
    root,
    height=7,
    width=75,
    font=("Arial", 12),
    relief="solid",
    borderwidth=1,
    padx=10,
    pady=10
)
input_text.pack(padx=50)

#  TRANSLATION FUNCTION 

def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter some text.")
        return

    language_codes = {
        "English": "en",
        "Urdu": "ur",
        "Arabic": "ar",
        "Turkish": "tr",
        "Hindi": "hi",
        "French": "fr",
        "Spanish": "es",
        "German": "de"
    }

    source = language_codes[source_language.get()]
    target = language_codes[target_language.get()]

    try:
        response = requests.post(
            API_URL,
            data={
                "q": text,
                "source": source,
                "target": target,
                "format": "text"
            },
            timeout=30
        )

        result = response.json()

        output_text.delete("1.0", tk.END)

        if response.status_code == 200:
            output_text.insert(
                tk.END,
                result["translatedText"]
            )
        else:
            output_text.insert(
                tk.END,
                "Translation failed: " +
                result.get("error", "Unknown error")
            )

    except requests.exceptions.ConnectionError:
        output_text.delete("1.0", tk.END)
        output_text.insert(
            tk.END,
            "Cannot connect to LibreTranslate. Please start the server."
        )

    except requests.exceptions.Timeout:
        output_text.delete("1.0", tk.END)
        output_text.insert(
            tk.END,
            "The translation request took too long."
        )

#  SWAP FUNCTION 

def swap_languages():
    source = source_language.get()
    target = target_language.get()

    source_language.set(target)
    target_language.set(source)

    input_content = input_text.get("1.0", tk.END)
    output_content = output_text.get("1.0", tk.END)

    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

    input_text.insert(tk.END, output_content)
    output_text.insert(tk.END, input_content)

# BUTTONS 

button_frame = tk.Frame(
    root,
    bg="#f4f7fb"
)
button_frame.pack(pady=18)

swap_button = tk.Button(
    button_frame,
    text="🔄 Swap",
    font=("Arial", 11, "bold"),
    bg="#ffffff",
    fg="#1f3c88",
    padx=22,
    pady=8,
    relief="solid",
    borderwidth=1,
    cursor="hand2",
    command=swap_languages
)
swap_button.pack(side=tk.LEFT, padx=8)

translate_button = tk.Button(
    button_frame,
    text="Translate",
    font=("Arial", 11, "bold"),
    bg="#1f3c88",
    fg="white",
    padx=28,
    pady=8,
    relief="flat",
    cursor="hand2",
    command=translate_text
)
translate_button.pack(side=tk.LEFT, padx=8)

# OUTPUT

tk.Label(
    root,
    text="Translation",
    font=("Arial", 12, "bold"),
    bg="#f4f7fb",
    fg="#333333"
).pack(anchor="w", padx=50, pady=(5, 7))

output_text = tk.Text(
    root,
    height=7,
    width=75,
    font=("Arial", 12),
    relief="solid",
    borderwidth=1,
    padx=10,
    pady=10
)
output_text.pack(padx=50)



root.mainloop()