import tkinter as tk
from tkinter import ttk

class BMICalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.age_label = tk.Label(self.master, text="Age:")
        self.age_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=0, column=1, padx=10, pady=5)

        self.gender_label = tk.Label(self.master, text="Gender:")
        self.gender_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(self.master, textvariable=self.gender_var, values=["Male", "Female"])
        self.gender_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.gender_combobox.current(0)

        self.height_label = tk.Label(self.master, text="Height (cm):")
        self.height_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.height_entry = tk.Entry(self.master)
        self.height_entry.grid(row=2, column=1, padx=10, pady=5)

        self.weight_label = tk.Label(self.master, text="Weight (kg):")
        self.weight_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=3, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_bmi)
        self.calculate_button.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_entries)
        self.reset_button.grid(row=5, column=0, padx=10, pady=5, columnspan=2)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=6, column=0, padx=10, pady=5, columnspan=2)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=7, column=0, padx=10, pady=5, columnspan=2)

        self.master.grid_columnconfigure(1, weight=1)

    def calculate_bmi(self):
        try:
            age = int(self.age_entry.get())
            gender = self.gender_var.get()
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / ((height / 100) ** 2)
            bmi_category = self.get_bmi_category(bmi)
            self.result_label.config(text=f"BMI: {bmi:.2f}, Category: {bmi_category}")
        except ValueError:
            self.result_label.config(text="Invalid input")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def reset_entries(self):
        self.age_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.result_label.config(text="")

def main():
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()