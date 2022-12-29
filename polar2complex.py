import sys
import math
import tkinter as tk
import pyperclip

class PolarComplexConverter:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()

        intro = tk.Label(frame, text='Welcome to NAGF Polar2complex Converter for MATLAB\nThis program will convert any given numbers from polar form to rectangular or vice versa in MATLAB format')
        intro.pack(pady=(0, 25))

        self.intro2 = tk.Label(frame, text='Please choose a conversion mode:')
        self.intro2.pack(pady=(0, 5))

        self.polar_to_complex_button = tk.Button(frame, text="Polar to Complex", command=self.choose_polar_to_complex)
        self.polar_to_complex_button.pack(pady=(0, 5))

        self.complex_to_polar_button = tk.Button(frame, text="Complex to Polar", command=self.choose_complex_to_polar)
        self.complex_to_polar_button.pack(pady=(0, 5))

        self.magnitude_label = tk.Label(text="Enter the magnitude:")
        self.magnitude_entry = tk.Entry()
        self.angle_label = tk.Label(text="Enter the angle (in radians):")
        self.angle_entry = tk.Entry()

        self.real_label = tk.Label(text="Enter the real part:")
        self.real_entry = tk.Entry()
        self.imaginary_label = tk.Label(text="Enter the imaginary part:")
        self.imaginary_entry = tk.Entry()

        self.calculate_button_1 = tk.Button(text="Calculate", command=self.convert_polar_to_complex)
        self.calculate_button_2 = tk.Button(text="Calculate", command=self.convert_complex_to_polar)

        self.result_label = tk.Label(text="")

        self.copy_button = tk.Button(text="Copy Results", command=self.copy_results)

        self.exit_button = tk.Button(text='Exit', command=self.exit_program)
        self.exit_button.pack()

    def choose_polar_to_complex(self):
        self.intro2['text'] = 'Polar to complex conversion selected'

        self.magnitude_label.pack_forget()
        self.magnitude_entry.pack_forget()
        self.angle_label.pack_forget()
        self.angle_entry.pack_forget()
        self.real_label.pack_forget()
        self.real_entry.pack_forget()
        self.imaginary_label.pack_forget()
        self.imaginary_entry.pack_forget()
        self.calculate_button_1.pack_forget()
        self.calculate_button_2.pack_forget()
        self.result_label.pack_forget()
        self.copy_button.pack_forget()
        self.exit_button.pack_forget()

        self.magnitude_label.pack()
        self.magnitude_entry.pack(pady=(0, 5))

        self.angle_label.pack()
        self.angle_entry.pack(pady=(0, 10))

        self.calculate_button_1.pack(pady=(0, 5))

        self.result_label.pack(pady=(0, 5))

        self.copy_button.pack(pady=(0, 5))

        self.exit_button.pack()

    def choose_complex_to_polar(self):
        self.intro2['text'] = 'Complex to polar conversion selected'

        self.magnitude_label.pack_forget()
        self.magnitude_entry.pack_forget()
        self.angle_label.pack_forget()
        self.angle_entry.pack_forget()
        self.real_label.pack_forget()
        self.real_entry.pack_forget()
        self.imaginary_label.pack_forget()
        self.imaginary_entry.pack_forget()
        self.calculate_button_1.pack_forget()
        self.calculate_button_2.pack_forget()
        self.result_label.pack_forget()
        self.copy_button.pack_forget()
        self.exit_button.pack_forget()

        self.real_label.pack()
        self.real_entry.pack(pady=(0, 5))

        self.imaginary_label.pack()
        self.imaginary_entry.pack(pady=(0, 10))

        self.calculate_button_2.pack(pady=(0, 5))

        self.result_label.pack(pady=(0, 5))

        self.copy_button.pack(pady=(0, 5))

        self.exit_button.pack()

    def convert_polar_to_complex(self):
        try:
            self.copy_button.pack_forget()
            self.exit_button.pack_forget()
            r = float(self.magnitude_entry.get())
            theta = float(self.angle_entry.get())

            real = r * math.cos(theta)
            imag = r * math.sin(theta)

            result = f"{real} + {imag}i"
            self.result_label.config(text=result)
            self.result_label.pack()

            self.copy_button.pack(pady=(0, 5))
            self.exit_button.pack()
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")
            self.result_label.pack()

            self.copy_button.pack(pady=(0, 5))
            self.exit_button.pack()

    def convert_complex_to_polar(self):
        try:
            self.copy_button.pack_forget()
            self.exit_button.pack_forget()
            real = float(self.real_entry.get())
            imag = float(self.imaginary_entry.get())

            r = math.sqrt(real**2 + imag**2)
            theta = math.atan2(imag, real)

            result = f"{r}, {theta}"
            self.result_label.config(text=result)
            self.result_label.pack()

            self.copy_button.pack(pady=(0, 5))
            self.exit_button.pack()
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")
            self.result_label.pack()

            self.copy_button.pack(pady=(0, 5))
            self.exit_button.pack()

    def copy_results(self):
        result = self.result_label.cget("text")
        pyperclip.copy(result)

    def exit_program(self):
        root.destroy()
        sys.exit()

root = tk.Tk()
root.wm_iconbitmap('icon.ico')
root.title('Polar2complex converter')
root.geometry('600x400')
converter = PolarComplexConverter(root)

root.mainloop()

# https://github.com/nagonzalezf
