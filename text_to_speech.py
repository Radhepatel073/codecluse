import pyttsx3
import tkinter as tk
from tkinter import ttk

class TextToSpeechApp:
    def __init__(self, root):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Default rate
        self.engine.setProperty('volume', 1.0)  # Default volume

        self.root = root
        self.root.title("Text to Speech Converter")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Text input
        self.text_label = tk.Label(self.root, text="Enter text:")
        self.text_label.pack(pady=5)

        self.text_entry = tk.Text(self.root, height=10, width=50)
        self.text_entry.pack(pady=5)

        # Volume slider
        self.volume_label = tk.Label(self.root, text="Volume:")
        self.volume_label.pack(pady=5)

        self.volume_slider = tk.Scale(self.root, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.1)
        self.volume_slider.set(1.0)  # Default volume
        self.volume_slider.pack(pady=5)

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert to Speech", command=self.convert_to_speech)
        self.convert_button.pack(pady=10)

    def convert_to_speech(self):
        # Get text and volume
        text = self.text_entry.get("1.0", tk.END).strip()
        volume = self.volume_slider.get()
        
        if text:
            # Set the volume and convert text to speech
            self.engine.setProperty('volume', volume)
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            tk.messagebox.showwarning("Input Error", "Please enter some text.")

def main():
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
