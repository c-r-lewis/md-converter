import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog, ttk
import pypandoc

def convert_text():
    input_text = input_box.get("1.0", tk.END)
    if not input_text.strip():
        messagebox.showwarning("Input Error", "The input text box is empty.")
        return

    output_format = format_var.get()

    if output_format in ["docx", "odt"]:
        # For docx and odt, save to a file
        output_path = filedialog.asksaveasfilename(defaultextension=f".{output_format}",
                                                   filetypes=[(f"{output_format.upper()} Files", f"*.{output_format}")])
        if not output_path:
            return
        try:
            pypandoc.convert_text(input_text, output_format, format='md', outputfile=output_path)
            messagebox.showinfo("Success", f"Text converted successfully and saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        # For HTML, display in the output box
        try:
            output_text = pypandoc.convert_text(input_text, output_format, format='md')
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, output_text)
            messagebox.showinfo("Success", f"Text converted successfully to {output_format.upper()} format!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def copy_to_clipboard():
    converted_text = output_box.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(converted_text)
    messagebox.showinfo("Copied", "Converted text has been copied to the clipboard!")

def clear_input():
    input_box.delete("1.0", tk.END)

def update_format_menu(*args):
    # Update the menu to ensure all options are visible
    menu = format_menu["menu"]
    menu.delete(0, "end")
    for option in ["html", "odt", "docx"]:
        menu.add_command(label=option, command=tk._setit(format_var, option))

# Set up the main application window
root = tk.Tk()
root.title("Markdown Converter")
root.geometry("600x600")

# Use a style for better aesthetics
style = ttk.Style()
style.configure("TLabel", padding=6, relief="flat", background="#f0f0f0", font=("Helvetica", 10))
style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Helvetica", 10))
style.map("TButton", background=[("active", "#45a049")])

# Create and set the variable for the output format
format_var = tk.StringVar(value="html")

# Create UI elements with improved layout
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

input_label = ttk.Label(frame, text="Enter Markdown text:")
input_label.grid(row=0, column=0, pady=10, sticky=tk.W)

input_box = scrolledtext.ScrolledText(frame, height=10, width=50, wrap=tk.WORD, font=("Helvetica", 10))
input_box.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))

convert_button = ttk.Button(frame, text="Convert Text", command=convert_text)
convert_button.grid(row=2, column=0, pady=10, sticky=tk.W)

clear_button = ttk.Button(frame, text="Clear Input", command=clear_input)
clear_button.grid(row=2, column=0, pady=10, padx=100, sticky=tk.E)

format_label = ttk.Label(frame, text="Select output format:")
format_label.grid(row=3, column=0, pady=5, sticky=tk.W)

# Define format_menu before the update_format_menu function
format_menu = ttk.OptionMenu(frame, format_var, "html", "odt", "docx")
format_menu.grid(row=4, column=0, pady=5, sticky=tk.W)

# Trace changes to format_var after format_menu is defined
format_var.trace("w", update_format_menu)

output_label = ttk.Label(frame, text="Converted text:")
output_label.grid(row=5, column=0, pady=10, sticky=tk.W)

output_box = scrolledtext.ScrolledText(frame, height=10, width=50, wrap=tk.WORD, font=("Helvetica", 10))
output_box.grid(row=6, column=0, pady=5, sticky=(tk.W, tk.E))

copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, pady=10, sticky=tk.W)

# Configure grid weights for responsive design
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(6, weight=1)

# Run the application
root.mainloop()
