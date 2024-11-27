import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL = "http://127.0.0.1:8000"  # Replace with your Django API's base URL

# Tkinter App Class
class MeepApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meep API Client")
        self.root.geometry("600x400")
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Entry for search
        self.search_label = ttk.Label(self.root, text="Search Meeps:")
        self.search_label.pack(pady=5)

        self.search_entry = ttk.Entry(self.root, width=40)
        self.search_entry.pack(pady=5)

        self.search_button = ttk.Button(self.root, text="Search", command=self.search_meeps)
        self.search_button.pack(pady=5)

        # Text box for results
        self.results_box = tk.Text(self.root, height=15, width=70)
        self.results_box.pack(pady=10)

        # Create buttons for operations
        self.like_button = ttk.Button(self.root, text="Like a Meep", command=self.like_meep)
        self.like_button.pack(pady=5)

        self.follow_button = ttk.Button(self.root, text="Follow User", command=self.follow_user)
        self.follow_button.pack(pady=5)

    def search_meeps(self):
        """Search for Meeps"""
        query = self.search_entry.get()
        if not query:
            messagebox.showwarning("Input Required", "Please enter a search query.")
            return
        
        url = f"{BASE_URL}/meeps/search/"
        data = {"search": query}
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                meeps = response.json()
                self.results_box.delete("1.0", tk.END)
                for meep in meeps:
                    self.results_box.insert(tk.END, f"ID: {meep['id']} - {meep['body']} (Likes: {meep['likes_count']})\n")
            else:
                messagebox.showerror("Error", f"Failed to search meeps. Status code: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def like_meep(self):
        """Like a Meep by ID"""
        meep_id = tk.simpledialog.askinteger("Like Meep", "Enter Meep ID to Like:")
        if not meep_id:
            return

        url = f"{BASE_URL}/meeps/{meep_id}/like/"
        try:
            response = requests.post(url, headers={"Authorization": "Bearer <f0c30e056902b45fc55a89c0c0d729409ed9f753>"})  # Add auth if needed
            if response.status_code == 200:
                messagebox.showinfo("Success", response.json().get("message", "Action completed successfully."))
            else:
                messagebox.showerror("Error", f"Failed to like meep. Status code: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def follow_user(self):
        """Follow a User by Profile ID"""
        user_id = tk.simpledialog.askinteger("Follow User", "Enter Profile ID to Follow:")
        if not user_id:
            return

        url = f"{BASE_URL}/profile/follow/{user_id}/"
        try:
            response = requests.post(url, headers={"Authorization": "Bearer <f0c30e056902b45fc55a89c0c0d729409ed9f753>"})  # Add auth if needed
            if response.status_code == 200:
                messagebox.showinfo("Success", response.json().get("message", "Action completed successfully."))
            else:
                messagebox.showerror("Error", f"Failed to follow user. Status code: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Main Tkinter loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MeepApp(root)
    root.mainloop()
