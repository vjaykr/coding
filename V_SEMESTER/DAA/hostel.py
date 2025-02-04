import tkinter as tk
from tkinter import ttk, messagebox

class Hostel:
    def __init__(self):
        self.rooms = {}
        self.students = {}
        self.months = ["January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"]
    
    def add_room(self, room_no, bed_count):
        if room_no not in self.rooms:
            self.rooms[room_no] = [None] * bed_count
            return True
        else:
            return False  # Room already exists
    
    def allocate_bed(self, room_no, bed_no, student_id):
        if room_no in self.rooms:
            if bed_no < len(self.rooms[room_no]) and self.rooms[room_no][bed_no] is None:
                self.rooms[room_no][bed_no] = student_id
                return True
            else:
                return False  # Bed already occupied or out of range
        else:
            return False  # Room does not exist
    
    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = name
            return True
        else:
            return False  # Student already exists
    
    def pay_fee(self, student_id, month, amount):
        if student_id in self.students and month in self.months:
            # In a real system, you would likely record payments somewhere
            print(f"Fee of {amount} paid for {month} by {self.students[student_id]}")
            return True
        else:
            return False  # Student or month not found


class HostelManagementApp:
    def __init__(self, root, hostel):
        self.root = root
        self.root.title("Hostel Management System")
        self.hostel = hostel
        
        # Frames
        self.admin_panel_frame = ttk.Frame(self.root)
        self.registration_fee_frame = ttk.Frame(self.root)
        
        # Notebook (Tabbed Interface)
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.pack(expand=1, fill="both")
        
        self.admin_panel_tab = ttk.Frame(self.tabControl)
        self.registration_fee_tab = ttk.Frame(self.tabControl)
        
        self.tabControl.add(self.admin_panel_tab, text='Admin Panel')
        self.tabControl.add(self.registration_fee_tab, text='Registration & Fee')
        
        # Switching between tabs
        self.tabControl.bind("<<NotebookTabChanged>>", self.on_tab_selected)
        
        # Admin Panel
        self.create_admin_panel_ui()
        
        # Registration & Fee Panel
        self.create_registration_fee_ui()
        
        # Show Admin Panel by default
        self.show_admin_panel()
    
    def on_tab_selected(self, event):
        current_tab = event.widget.select()
        tab_text = event.widget.tab(current_tab, "text")
        
        if tab_text == "Admin Panel":
            self.show_admin_panel()
        elif tab_text == "Registration & Fee":
            self.show_registration_fee_panel()
    
    def show_admin_panel(self):
        self.admin_panel_frame.pack(fill='both', expand=True)
        self.registration_fee_frame.pack_forget()
    
    def show_registration_fee_panel(self):
        self.registration_fee_frame.pack(fill='both', expand=True)
        self.admin_panel_frame.pack_forget()
    
    def create_admin_panel_ui(self):
        # Admin Panel UI
        ttk.Label(self.admin_panel_frame, text="Admin Panel", font=('Helvetica', 18)).pack(pady=10)
        
        ttk.Button(self.admin_panel_frame, text="Add Room", command=self.add_room_window).pack(pady=5)
        ttk.Button(self.admin_panel_frame, text="Allocate Bed", command=self.allocate_bed_window).pack(pady=5)
        ttk.Button(self.admin_panel_frame, text="Add Student", command=self.add_student_window).pack(pady=5)
        ttk.Button(self.admin_panel_frame, text="Manage Fees", command=self.manage_fees_window).pack(pady=5)
    
    def create_registration_fee_ui(self):
        # Registration & Fee Panel UI
        ttk.Label(self.registration_fee_frame, text="Registration & Fee Panel", font=('Helvetica', 18)).pack(pady=10)
        
        ttk.Button(self.registration_fee_frame, text="Register Student", command=self.register_student_window).pack(pady=5)
        ttk.Button(self.registration_fee_frame, text="Pay Fee", command=self.pay_fee_window).pack(pady=5)
    
    def add_room_window(self):
        # Implement the Add Room functionality
        pass
    
    def allocate_bed_window(self):
        # Implement the Allocate Bed functionality
        pass
    
    def add_student_window(self):
        # Implement the Add Student functionality
        pass
    
    def manage_fees_window(self):
        # Implement the Manage Fees functionality
        pass
    
    def register_student_window(self):
        # Implement the Register Student functionality
        pass
    
    def pay_fee_window(self):
        # Implement the Pay Fee functionality
        pass


if __name__ == "__main__":
    hostel = Hostel()
    
    root = tk.Tk()
    app = HostelManagementApp(root, hostel)
    root.mainloop()
