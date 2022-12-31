import tkinter as tk

# Set FICA and SDI tax rates
FICA_RATE = 0.062
SDI_RATE = 0.01

def calculate_payroll():
  # Get values from input fields
  hourly_rate = float(hourly_rate_entry.get())
  hours = float(hours_entry.get())

  # Calculate gross pay
  gross_pay = hourly_rate * hours
  # Calculate FICA tax
  fica_tax = gross_pay * FICA_RATE
  # Calculate SDI tax
  sdi_tax = gross_pay * SDI_RATE
  # Calculate net pay
  net_pay = gross_pay - fica_tax - sdi_tax

  # Display results in output fields
  gross_pay_output.config(text=f"{gross_pay:.2f}")
  fica_tax_output.config(text=f"{fica_tax:.2f}")
  sdi_tax_output.config(text=f"{sdi_tax:.2f}")
  net_pay_output.config(text=f"{net_pay:.2f}")

# Create the main window
window = tk.Tk()
window.title("Payroll Calculator")

# Create input fields
tk.Label(window, text="Hourly rate:").grid(row=0, column=0)
hourly_rate_entry = tk.Entry(window)
hourly_rate_entry.grid(row=0, column=1)

tk.Label(window, text="Hours:").grid(row=1, column=0)
hours_entry = tk.Entry(window)
hours_entry.grid(row=1, column=1)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_payroll)
calculate_button.grid(row=2, column=0, columnspan=2)

# Create output fields
tk.Label(window, text="Gross pay:").grid(row=3, column=0)
gross_pay_output = tk.Label(window, text="")
gross_pay_output.grid(row=3, column=1)

tk.Label(window, text="FICA tax:").grid(row=4, column=0)
fica_tax_output = tk.Label(window, text="")
fica_tax_output.grid(row=4, column=1)

tk.Label(window, text="SDI tax:").grid(row=5, column=0)
sdi_tax_output = tk.Label(window, text="")
sdi_tax_output.grid(row=5, column=1)

tk.Label(window, text="Net pay:").grid(row=6, column=0)
net_pay_output = tk.Label(window, text="")
net_pay_output.grid(row=6, column=1)

# Run the main loop
window.mainloop()
