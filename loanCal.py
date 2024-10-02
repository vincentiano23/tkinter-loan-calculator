import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_loan():
    try:
     
        loan_amount = float(entry_loan_amount.get())
        interest_rate = float(entry_interest_rate.get()) / 100 / 12 
        loan_term = int(entry_loan_term.get()) * 12  
        
      
        if interest_rate == 0:
            monthly_payment = loan_amount / loan_term
        else:
            monthly_payment = loan_amount * interest_rate * (1 + interest_rate) ** loan_term / ((1 + interest_rate) ** loan_term - 1)
        
        total_payment_year = monthly_payment * 12
       
        result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
        total_payment_label.config(text=f"Total Payment (1 year): ${total_payment_year:.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def calculate_countdown():
    try:
        
        start_date_str = entry_start_date.get()
        repayment_period_days = int(entry_repayment_period.get())
        
     
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        
        end_date = start_date + timedelta(days=repayment_period_days)
        
        today = datetime.now()
        remaining_days = (end_date - today).days
        
        if remaining_days > 0:
            countdown_label.config(text=f"Days Remaining: {remaining_days} days")
        else:
            countdown_label.config(text="Loan period has ended.")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid dates and repayment period.")

def submit_feedback():
    feedback = entry_feedback.get()
    if feedback:
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        entry_feedback.delete(0, tk.END)
    else:
        messagebox.showerror("Input Error", "Please enter your feedback before submitting.")


root = tk.Tk()
root.title("Loan Calculator")
root.geometry("400x400")
root.configure(bg="#00FFFF")


label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

label_loan_amount = ttk.Label(root, text="Loan Amount:", font=label_font, background="#f0f0f0")
label_loan_amount.pack(pady=10)
entry_loan_amount = ttk.Entry(root, font=entry_font, justify="center")
entry_loan_amount.pack(pady=10)

label_interest_rate = ttk.Label(root, text="Interest Rate (Annual %):", font=label_font, background="#f0f0f0")
label_interest_rate.pack(pady=10)
entry_interest_rate = ttk.Entry(root, font=entry_font, justify="center")
entry_interest_rate.pack(pady=10)



label_loan_term = ttk.Label(root, text="Loan Term (Years):", font=label_font, background="#f0f0f0")
label_loan_term.pack(pady=10)
entry_loan_term = ttk.Entry(root, font=entry_font, justify="center")
entry_loan_term.pack(pady=10)

label_start_date = ttk.Label(root, text="Loan Start Date (YYYY-MM-DD):", font=label_font, background="#f0f0f0")
label_start_date.pack(pady=10)
entry_start_date = ttk.Entry(root, font=entry_font, justify="center")
entry_start_date.pack(pady=10)

label_repayment_period = ttk.Label(root, text="Repayment Period (Days):", font=label_font, background="#f0f0f0")
label_repayment_period.pack(pady=10)
entry_repayment_period = ttk.Entry(root, font=entry_font, justify="center")
entry_repayment_period.pack(pady=10)


calculate_button = ttk.Button(root, text="Calculate", command=calculate_loan, style="TButton")
calculate_button.pack(pady=20)

result_label = ttk.Label(root, text="Monthly Payment: $0.00", font=label_font, background="#f0f0f0")
result_label.pack(pady=20)

total_payment_label = ttk.Label(root, text="Total Payment (1 year): $0.00", font=label_font, background="#f0f0f0")
total_payment_label.pack(pady=10)

countdown_button = ttk.Button(root, text="Calculate Countdown", command=calculate_countdown, style="TButton")
countdown_button.pack(padx=10)

countdown_label = ttk.Label(root, text="Days Remaining: N/A", font=label_font, background="#f0f0f0")
countdown_label.pack(pady=10)

label_feedback = ttk.Label(root, text="Feedback on Calculator:", font=label_font, background="#f0f0f0")
label_feedback.pack(pady=10)
entry_feedback = ttk.Entry(root, font=entry_font, width=40)
entry_feedback.pack(pady=10)

feedback_button = ttk.Button(root, text="Submit Feedback", command=submit_feedback, style="TButton")
feedback_button.pack(pady=15)


style = ttk.Style()
style.configure("TButton", font=button_font, padding=4)

root.mainloop()
