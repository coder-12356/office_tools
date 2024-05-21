import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class JobExperienceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Experience Calculator")

        self.experiences = []

        self.create_widgets()
    
    def create_widgets(self):
        # Labels and entries for Start Date, Exit Date, and Company Name
        tk.Label(self.root, text="Company Name:").grid(row=0, column=0)
        self.company_name_entry = tk.Entry(self.root)
        self.company_name_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Start Date (DDMMYYYY):").grid(row=1, column=0)
        self.start_date_entry = tk.Entry(self.root)
        self.start_date_entry.grid(row=1, column=1)
        
        tk.Label(self.root, text="Exit Date (DDMMYYYY):").grid(row=2, column=0)
        self.exit_date_entry = tk.Entry(self.root)
        self.exit_date_entry.grid(row=2, column=1)

        
        
        # Buttons to add and calculate experiences
        self.add_button = tk.Button(self.root, text="Add More Company", command=self.add_experience)
        self.add_button.grid(row=3, column=1, columnspan=1, pady=10)
        
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_experience)
        self.calculate_button.grid(row=3, column=0, columnspan=1, pady=10)
        
        # Frame to list added experiences
        self.experience_list_frame = tk.Frame(self.root)
        self.experience_list_frame.grid(row=5, column=0, columnspan=2)
        
        # Save button
        self.save_button = tk.Button(self.root, text="Save", command=self.save_experience)
        self.save_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.save_button.grid_remove()

    def add_experience(self):
        start_date = self.start_date_entry.get()
        exit_date = self.exit_date_entry.get()
        company_name = self.company_name_entry.get()
        
        # Validate the dates
        try:
            start_date_dt = datetime.strptime(start_date, "%d%m%Y")
            exit_date_dt = datetime.strptime(exit_date, "%d%m%Y")
            if start_date_dt > exit_date_dt:
                raise ValueError("Start date must be before exit date")
        except ValueError as e:
            messagebox.showerror("Invalid Date", f"Error in dates: {e}")
            return
        
        # Calculate individual company experience
        days = (exit_date_dt - start_date_dt).days
        years, remainder = divmod(days, 365)
        months, days = divmod(remainder, 30)
        experience_str = f"{years} years, {months} months, and {days} days"
        
        self.experiences.append((start_date, exit_date, company_name, experience_str))
        self.update_experience_list()
        
        # Clear entries
        self.start_date_entry.delete(0, tk.END)
        self.exit_date_entry.delete(0, tk.END)
        self.company_name_entry.delete(0, tk.END)
    
    def update_experience_list(self):
        for widget in self.experience_list_frame.winfo_children():
            widget.destroy()
        
        for idx, (start, end, company, exp) in enumerate(self.experiences):
            tk.Label(self.experience_list_frame, text=f"{company}: {start} to {end} ({exp})").grid(row=idx, column=0)
            tk.Button(self.experience_list_frame, text="Remove", command=lambda idx=idx: self.remove_experience(idx)).grid(row=idx, column=1)
    
    def remove_experience(self, idx):
        del self.experiences[idx]
        self.update_experience_list()
    
    def calculate_experience(self):
        total_days = 0
        for start, end, _, _ in self.experiences:
            start_date_dt = datetime.strptime(start, "%d%m%Y")
            exit_date_dt = datetime.strptime(end, "%d%m%Y")
            total_days += (exit_date_dt - start_date_dt).days
        
        years, remainder = divmod(total_days, 365)
        months, days = divmod(remainder, 30)
        
        self.total_experience_str = f"Total Experience: {years} years, {months} months, and {days} days"
        messagebox.showinfo("Total Experience", self.total_experience_str)
        self.save_button.grid()
    
    def save_experience(self):
        with open("experience_details.txt", "w") as file:
            for start, end, company, exp in self.experiences:
                file.write(f"{company}: {start} to {end} ({exp})\n")
            file.write("\n" + self.total_experience_str)
        messagebox.showinfo("Saved", "Experience details saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = JobExperienceCalculator(root)
    root.mainloop()
