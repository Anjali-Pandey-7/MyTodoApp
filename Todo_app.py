import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import tkinter.font as tkFont
from tkcalendar import DateEntry
import json
import os
from datetime import datetime, timedelta

class EnhancedTodoApp:
    # ========== COLOR THEMES ==========
    THEMES = {
        "Girly Pink": {
            "primary": "#ff69b4",
            "light": "#ffb6c1",
            "bg": "#fff5f8",
            "dark": "#ff1493",
            "accent": "#da70d6",
            "completed": "#90EE90",
            "delete": "#ff6b6b"
        },
        "Dark Mode": {
            "primary": "#1e1e1e",
            "light": "#333333",
            "bg": "#0d0d0d",
            "dark": "#2d2d2d",
            "accent": "#bb86fc",
            "completed": "#81c784",
            "delete": "#ff6b6b"
        },
        "Ocean Blue": {
            "primary": "#0066cc",
            "light": "#66b3ff",
            "bg": "#e6f2ff",
            "dark": "#0052a3",
            "accent": "#00ccff",
            "completed": "#00ff00",
            "delete": "#ff4444"
        },
        "Purple Vibes": {
            "primary": "#9370db",
            "light": "#dda0dd",
            "bg": "#f3e5f5",
            "dark": "#663399",
            "accent": "#9932cc",
            "completed": "#90ee90",
            "delete": "#ff6b6b"
        },
        "Sunset": {
            "primary": "#ff7f50",
            "light": "#ffa07a",
            "bg": "#fff8dc",
            "dark": "#ff6347",
            "accent": "#ffa500",
            "completed": "#90ee90",
            "delete": "#ff4444"
        },
        "Mint Fresh": {
            "primary": "#20b2aa",
            "light": "#7fffd4",
            "bg": "#f0ffff",
            "dark": "#008080",
            "accent": "#3cb371",
            "completed": "#90ee90",
            "delete": "#ff6b6b"
        }
    }
    
    def __init__(self, root):
        """Initialize the Enhanced To-Do List application"""
        self.root = root
        self.root.title("✨ My Beautiful To-Do List ✨")
        self.root.geometry("750x820")
        
        # Files
        self.tasks_file = "tasks.json"
        self.config_file = "config.json"
        
        # Store tasks
        self.tasks = []
        
        # Load configuration (theme preference)
        self.current_theme = self.load_config()
        self.colors = self.THEMES[self.current_theme].copy()
        
        # Update window background
        self.root.configure(bg=self.colors["bg"])
        
        # Create custom fonts
        self.title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.subtitle_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        self.task_font = tkFont.Font(family="Helvetica", size=10)
        
        # Build the UI
        self.create_ui()
        
        # Load tasks from file
        self.load_tasks()
        
        # Update the display
        self.update_listbox()
    
    def load_config(self):
        """Load configuration including theme preference"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    return config.get('theme', 'Girly Pink')
        except:
            pass
        return 'Girly Pink'
    
    def save_config(self):
        """Save configuration including theme preference"""
        try:
            config = {'theme': self.current_theme}
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            messagebox.showerror("Config Error", f"Failed to save config: {e}")
    
    def create_ui(self):
        """Create all UI elements"""
        
        # ===== HEADER SECTION =====
        header_frame = tk.Frame(self.root, bg=self.colors["primary"], height=100)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Top bar with title and settings button
        top_bar = tk.Frame(header_frame, bg=self.colors["primary"])
        top_bar.pack(fill=tk.X, padx=15, pady=(10, 0))
        
        title_label = tk.Label(
            top_bar,
            text="✨ My To-Do List ✨",
            font=self.title_font,
            bg=self.colors["primary"],
            fg="white"
        )
        title_label.pack(side=tk.LEFT)
        
        # Settings button
        settings_button = tk.Button(
            top_bar,
            text="⚙️ Theme",
            command=self.open_theme_settings,
            font=("Helvetica", 10, "bold"),
            bg=self.colors["light"],
            fg=self.colors["dark"],
            padx=10,
            pady=5,
            border=0,
            relief=tk.FLAT,
            cursor="hand2"
        )
        settings_button.pack(side=tk.RIGHT)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Track your tasks with style 💕 | Theme: " + self.current_theme,
            font=("Helvetica", 10),
            bg=self.colors["primary"],
            fg="white"
        )
        subtitle_label.pack(pady=(5, 10))
        self.subtitle_label = subtitle_label  # Store reference to update later
        
        # ===== INPUT SECTION =====
        input_frame = tk.Frame(self.root, bg=self.colors["bg"])
        input_frame.pack(fill=tk.X, padx=20, pady=15)
        
        input_label = tk.Label(
            input_frame,
            text="✍️ Add a new task:",
            font=self.subtitle_font,
            bg=self.colors["bg"],
            fg=self.colors["primary"]
        )
        input_label.pack(anchor=tk.W)
        
        # Task input
        self.task_entry = tk.Entry(
            input_frame,
            font=self.task_font,
            width=40,
            bg="white",
            fg="#333333",
            border=2,
            relief=tk.RIDGE
        )
        self.task_entry.pack(fill=tk.X, pady=(8, 10))
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        # Due date section
        date_frame = tk.Frame(input_frame, bg=self.colors["bg"])
        date_frame.pack(fill=tk.X, pady=(0, 10))
        
        date_label = tk.Label(
            date_frame,
            text="📅 Due Date (optional):",
            font=("Helvetica", 9),
            bg=self.colors["bg"],
            fg=self.colors["dark"]
        )
        date_label.pack(anchor=tk.W)
        
        # Date picker
        self.date_entry = DateEntry(
            input_frame,
            width=20,
            background=self.colors["primary"],
            foreground="white",
            borderwidth=2,
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            headersforeground="white",
            normalbackground="white",
            normalforeground=self.colors["primary"],
            weekendbackground=self.colors["light"],
            weekendforeground=self.colors["primary"],
            othermonthweforeground=self.colors["light"],
            othermonthwebackground=self.colors["bg"],
            disabledbg=self.colors["light"],
            disabledfg="#888888"
        )
        self.date_entry.pack(anchor=tk.W, pady=(5, 0))
        
        # Add task button
        add_button = tk.Button(
            input_frame,
            text="💖 Add Task",
            command=self.add_task,
            font=self.button_font,
            bg=self.colors["primary"],
            fg="white",
            padx=20,
            pady=8,
            border=0,
            relief=tk.FLAT,
            activebackground=self.colors["dark"],
            activeforeground="white",
            cursor="hand2"
        )
        add_button.pack(pady=(10, 0))
        
        # ===== TASKS LIST SECTION =====
        list_frame = tk.Frame(self.root, bg=self.colors["bg"])
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 15))
        
        list_label = tk.Label(
            list_frame,
            text="📋 Your Tasks:",
            font=self.subtitle_font,
            bg=self.colors["bg"],
            fg=self.colors["primary"]
        )
        list_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Create a frame with scrollbar for the task list
        scrollbar_frame = tk.Frame(list_frame, bg=self.colors["bg"])
        scrollbar_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(scrollbar_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(
            scrollbar_frame,
            font=self.task_font,
            height=12,
            yscrollcommand=scrollbar.set,
            bg="white",
            fg="#333333",
            selectmode=tk.SINGLE,
            border=2,
            relief=tk.RIDGE,
            activestyle='none',
            selectbackground=self.colors["light"],
            selectforeground=self.colors["dark"]
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # ===== ACTION BUTTONS SECTION =====
        button_frame = tk.Frame(self.root, bg=self.colors["bg"])
        button_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Complete button
        complete_button = tk.Button(
            button_frame,
            text="✓ Mark Completed",
            command=self.mark_completed,
            font=self.button_font,
            bg=self.colors["completed"],
            fg="#333333",
            padx=12,
            pady=8,
            border=0,
            relief=tk.FLAT,
            activebackground="#7CCD7C",
            cursor="hand2"
        )
        complete_button.pack(side=tk.LEFT, padx=(0, 8))
        
        # Edit button
        edit_button = tk.Button(
            button_frame,
            text="✏️ Edit",
            command=self.edit_task,
            font=self.button_font,
            bg=self.colors["accent"],
            fg="white",
            padx=12,
            pady=8,
            border=0,
            relief=tk.FLAT,
            activebackground=self.colors["dark"],
            cursor="hand2"
        )
        edit_button.pack(side=tk.LEFT, padx=(0, 8))
        
        # Delete button
        delete_button = tk.Button(
            button_frame,
            text="🗑 Delete",
            command=self.delete_task,
            font=self.button_font,
            bg=self.colors["delete"],
            fg="white",
            padx=12,
            pady=8,
            border=0,
            relief=tk.FLAT,
            activebackground="#ff5252",
            cursor="hand2"
        )
        delete_button.pack(side=tk.LEFT, padx=(0, 8))
        
        # Clear completed button
        clear_button = tk.Button(
            button_frame,
            text="🧹 Clear Done",
            command=self.clear_completed,
            font=self.button_font,
            bg=self.colors["light"],
            fg=self.colors["dark"],
            padx=12,
            pady=8,
            border=0,
            relief=tk.FLAT,
            activebackground=self.colors["light"],
            cursor="hand2"
        )
        clear_button.pack(side=tk.LEFT)
    
    def open_theme_settings(self):
        """Open theme selection window"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("⚙️ Theme Settings")
        settings_window.geometry("400x500")
        settings_window.configure(bg=self.colors["bg"])
        
        # Title
        title = tk.Label(
            settings_window,
            text="Choose Your Theme 🎨",
            font=self.title_font,
            bg=self.colors["bg"],
            fg=self.colors["primary"]
        )
        title.pack(pady=20)
        
        # Description
        desc = tk.Label(
            settings_window,
            text="Select a theme and click 'Apply' to change colors",
            font=("Helvetica", 10),
            bg=self.colors["bg"],
            fg="#666666"
        )
        desc.pack(pady=(0, 20))
        
        # Theme selection frame
        themes_frame = tk.Frame(settings_window, bg=self.colors["bg"])
        themes_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Variable to store selected theme
        theme_var = tk.StringVar(value=self.current_theme)
        
        # Create buttons for each theme
        for theme_name in self.THEMES.keys():
            theme_colors = self.THEMES[theme_name]
            
            # Create a frame for each theme option
            theme_option_frame = tk.Frame(themes_frame, bg="white", relief=tk.RIDGE, bd=2)
            theme_option_frame.pack(fill=tk.X, pady=8)
            
            # Left side: color preview
            preview_frame = tk.Frame(theme_option_frame, bg=theme_colors["bg"], width=50, height=50)
            preview_frame.pack(side=tk.LEFT, padx=10, pady=10)
            preview_frame.pack_propagate(False)
            
            # Middle: color bars
            colors_display = tk.Frame(preview_frame, bg=theme_colors["bg"])
            colors_display.pack(fill=tk.BOTH, expand=True)
            
            color1 = tk.Frame(colors_display, bg=theme_colors["primary"], height=25)
            color1.pack(fill=tk.X)
            color1.pack_propagate(False)
            
            color2 = tk.Frame(colors_display, bg=theme_colors["accent"], height=25)
            color2.pack(fill=tk.X)
            color2.pack_propagate(False)
            
            # Right side: theme name and radio button
            right_frame = tk.Frame(theme_option_frame, bg="white")
            right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            radio_button = tk.Radiobutton(
                right_frame,
                text=theme_name,
                variable=theme_var,
                value=theme_name,
                font=("Helvetica", 11, "bold"),
                bg="white",
                fg=self.colors["primary"],
                activebackground="white",
                selectcolor="white"
            )
            radio_button.pack(anchor=tk.W)
            
            # Show current theme
            if theme_name == self.current_theme:
                current_label = tk.Label(
                    right_frame,
                    text="✓ Current",
                    font=("Helvetica", 9),
                    bg="white",
                    fg=self.colors["primary"]
                )
                current_label.pack(anchor=tk.W)
        
        # Buttons
        button_frame = tk.Frame(settings_window, bg=self.colors["bg"])
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        apply_button = tk.Button(
            button_frame,
            text="✅ Apply Theme",
            command=lambda: self.apply_theme(theme_var.get(), settings_window),
            font=self.button_font,
            bg=self.colors["primary"],
            fg="white",
            padx=20,
            pady=10,
            border=0,
            relief=tk.FLAT,
            cursor="hand2"
        )
        apply_button.pack(side=tk.LEFT, padx=(0, 10))
        
        cancel_button = tk.Button(
            button_frame,
            text="❌ Cancel",
            command=settings_window.destroy,
            font=self.button_font,
            bg="#cccccc",
            fg="#333333",
            padx=20,
            pady=10,
            border=0,
            relief=tk.FLAT,
            cursor="hand2"
        )
        cancel_button.pack(side=tk.LEFT)
    
    def apply_theme(self, theme_name, settings_window):
        """Apply the selected theme"""
        self.current_theme = theme_name
        self.colors = self.THEMES[self.current_theme].copy()
        
        # Save the preference
        self.save_config()
        
        # Update UI colors - this requires recreating the UI
        messagebox.showinfo(
            "Theme Changed",
            f"Theme changed to {theme_name}!\n\nThe app will restart to apply changes."
        )
        
        # Close settings window
        settings_window.destroy()
        
        # Restart the app (close and reopen)
        self.root.destroy()
        root = tk.Tk()
        app = EnhancedTodoApp(root)
        root.mainloop()
    
    def add_task(self):
        """Add a new task to the list"""
        task_text = self.task_entry.get().strip()
        
        if not task_text:
            messagebox.showwarning("Empty Task", "Please enter a task! 💭")
            return
        
        if len(task_text) > 100:
            messagebox.showwarning("Task Too Long", "Task must be less than 100 characters! 😊")
            return
        
        due_date = self.date_entry.get_date().strftime("%Y-%m-%d")
        
        self.tasks.append({
            'name': task_text,
            'completed': False,
            'due_date': due_date
        })
        
        self.update_listbox()
        self.save_tasks()
        
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus()
        
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%m/%d/%Y"))
        
        messagebox.showinfo("Success", "Task added successfully! 💖")
    
    def update_listbox(self):
        """Update the listbox display with all tasks"""
        self.task_listbox.delete(0, tk.END)
        
        for index, task in enumerate(self.tasks):
            task_name = task['name']
            due_date = task.get('due_date', '')
            
            if not task['completed'] and due_date:
                task_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                today = datetime.now().date()
                if task_date < today:
                    status_indicator = "⚠️"
                elif task_date == today:
                    status_indicator = "🔔"
                else:
                    status_indicator = "📅"
            else:
                status_indicator = "📅" if due_date else ""
            
            if task['completed']:
                display_text = f"[✓] {task_name}"
                if due_date:
                    display_text += f" - {due_date}"
            else:
                display_text = f"[ ] {task_name}"
                if due_date:
                    display_text += f" - {status_indicator} {due_date}"
            
            self.task_listbox.insert(tk.END, display_text)
            
            if task['completed']:
                self.task_listbox.itemconfig(index, {'fg': '#888888'})
            else:
                if due_date:
                    task_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                    today = datetime.now().date()
                    if task_date < today:
                        self.task_listbox.itemconfig(index, {'fg': '#ff4444'})
                    elif task_date == today:
                        self.task_listbox.itemconfig(index, {'fg': self.colors["primary"]})
    
    def mark_completed(self):
        """Mark the selected task as completed"""
        selection = self.task_listbox.curselection()
        
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task! 👆")
            return
        
        index = selection[0]
        self.tasks[index]['completed'] = not self.tasks[index]['completed']
        
        self.update_listbox()
        self.save_tasks()
        self.task_listbox.selection_set(index)
        
        if self.tasks[index]['completed']:
            messagebox.showinfo("Done!", "Great job! Task completed! 🎉")
    
    def edit_task(self):
        """Edit the selected task"""
        selection = self.task_listbox.curselection()
        
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to edit! ✏️")
            return
        
        index = selection[0]
        task = self.tasks[index]
        
        new_name = simpledialog.askstring(
            "Edit Task",
            "Enter new task name:",
            initialvalue=task['name']
        )
        
        if new_name and new_name.strip():
            self.tasks[index]['name'] = new_name.strip()
            self.update_listbox()
            self.save_tasks()
            messagebox.showinfo("Updated", "Task updated successfully! 💕")
        elif new_name is not None:
            messagebox.showwarning("Empty Name", "Task name cannot be empty!")
    
    def delete_task(self):
        """Delete the selected task"""
        selection = self.task_listbox.curselection()
        
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to delete! 🗑")
            return
        
        index = selection[0]
        task_name = self.tasks[index]['name']
        
        response = messagebox.askyesno(
            "Confirm Delete",
            f"Delete this task?\n\n'{task_name}'"
        )
        
        if response:
            self.tasks.pop(index)
            self.update_listbox()
            self.save_tasks()
            messagebox.showinfo("Deleted", "Task deleted! 💔")
    
    def clear_completed(self):
        """Clear all completed tasks"""
        completed_count = sum(1 for task in self.tasks if task['completed'])
        
        if completed_count == 0:
            messagebox.showinfo("No Completed Tasks", "There are no completed tasks to clear! 😊")
            return
        
        response = messagebox.askyesno(
            "Clear Completed",
            f"Delete all {completed_count} completed task(s)?"
        )
        
        if response:
            self.tasks = [task for task in self.tasks if not task['completed']]
            self.update_listbox()
            self.save_tasks()
            messagebox.showinfo("Cleared", "All completed tasks removed! ✨")
    
    def save_tasks(self):
        """Save tasks to a JSON file"""
        try:
            with open(self.tasks_file, 'w') as f:
                json.dump(self.tasks, f, indent=4)
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            if os.path.exists(self.tasks_file):
                with open(self.tasks_file, 'r') as f:
                    self.tasks = json.load(f)
            else:
                self.tasks = []
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load tasks: {e}")
            self.tasks = []


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = EnhancedTodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()