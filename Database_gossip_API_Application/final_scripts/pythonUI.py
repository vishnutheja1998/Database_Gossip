import tkinter as tk
from tkinter import messagebox
import requests
import json

class PersonalizedGreeterApp:
    def __init__(self, master):
        self.master = master
        master.title("Personalized Greeter")
        master.geometry("300x150")
        master.configure(bg='#2C3E50')

        self.label_given_name = tk.Label(master, text="Given Name:", bg='#2C3E50', fg='#E74C3C')
        self.label_given_name.pack()

        self.entry_given_name = tk.Entry(master)
        self.entry_given_name.pack()

        self.label_surname = tk.Label(master, text="Surname:", bg='#2C3E50', fg='#E74C3C')
        self.label_surname.pack()

        self.entry_surname = tk.Entry(master)
        self.entry_surname.pack()

        self.process_button = tk.Button(master, text="Process", command=self.send_request, bg='#E74C3C', fg='white')
        self.process_button.pack(pady=10)

    def send_request(self):
        given_name = self.entry_given_name.get()
        surname = self.entry_surname.get()

        url = "https://syle9bawzl.execute-api.us-east-1.amazonaws.com/stg"
        headers = {"Content-Type": "application/json"}
        payload = json.dumps({
            "givenName": given_name,
            "surname": surname
        })

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            result = response.json()
            messagebox.showinfo("Response", result['body'])
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalizedGreeterApp(root)
    root.mainloop()
