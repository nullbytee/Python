import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, name, jabatan):
        self.name = name
        self.jabatan = jabatan

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

        self.root = tk.Tk()
        self.root.title("Employee Management System")

        self.name_label = tk.Label(self.root, text="Nama:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.jabatan_label = tk.Label(self.root, text="Jabatan:")
        self.jabatan_label.pack()
        self.jabatan_entry = tk.Entry(self.root)
        self.jabatan_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        self.display_button = tk.Button(self.root, text="Display Employees", command=self.display_employees)
        self.display_button.pack()

    def add_employee(self):
        name = self.name_entry.get()
        jabatan = self.jabatan_entry.get()

        if name and jabatan:
            employee = Employee(name, jabatan)
            self.employees.append(employee)
            messagebox.showinfo("Success", "Employee added successfully!")
            self.name_entry.delete(0, tk.END)
            self.jabatan_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and position!")

    def display_employees(self):
        if self.employees:
            employee_list = "Employees:\n"
            for employee in self.employees:
                employee_list += f"Nama: {employee.name}, Jabatan: {employee.jabatan}\n"
            messagebox.showinfo("Employees", employee_list)
        else:
            messagebox.showinfo("Employees", "No employees found!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.run()
