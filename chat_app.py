import tkinter as tk

def send_message():

    message = message_entry.get()

    if message != "":

        chat_box.insert(tk.END, "You: " + message + "\n")

        if message.lower() == "hello":
            reply = "Hi!"
        elif message.lower() == "how are you":
            reply = "I am Fine."
        elif message.lower() == "what is your name":
            reply = "My name is ChatBot."
        elif message.lower() == "bye":
            reply = "Goodbye!"
        else:
            reply = "Sorry, I don't understand."

        chat_box.insert(tk.END, "Bot: " + reply + "\n\n")

        message_entry.delete(0, tk.END)

def clear_chat():

    chat_box.delete(1.0, tk.END)

window = tk.Tk()

window.title("AI Chat Application")

window.geometry("600x600")

window.config(bg="black")

heading = tk.Label(
    window,
    text="AI Chat Application",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="lime"
)

heading.pack(pady=10)

chat_box = tk.Text(
    window,
    height=20,
    width=60,
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12)
)

chat_box.pack(pady=10)

message_entry = tk.Entry(
    window,
    width=50,
    font=("Arial", 12)
)

message_entry.pack(pady=10)

send_button = tk.Button(
    window,
    text="Send",
    command=send_message,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
)

send_button.pack(pady=5)

clear_button = tk.Button(
    window,
    text="Clear Chat",
    command=clear_chat,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold")
)

clear_button.pack(pady=5)

message_entry.bind(
    "<Return>",
    lambda event: send_message()
)

window.mainloop()