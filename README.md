# 💖 Beautiful To-Do List App

A cute and colorful To-Do List application built with Python and Tkinter!

## ✨ Features

- ✅ Add, edit, and delete tasks
- 📅 Set due dates for tasks
- 🎨 **6 Beautiful Color Themes:**
  - 💖 Girly Pink
  - 🌙 Dark Mode
  - 🌊 Ocean Blue
  - 💜 Purple Vibes
  - 🌅 Sunset
  - 🍃 Mint Fresh
- 💾 Automatic saving (never lose your tasks!)
- 🎯 Theme preference saves automatically
- 📱 Works on Windows, Mac, and Linux

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/MyTodoApp.git
cd MyTodoApp
```

2. Install required library:
```bash
pip install -r requirements.txt
```

Or use auto-setup:
- **Windows:** Double-click `setup.bat`
- **Mac/Linux:** Run `bash setup.sh` in terminal

3. Run the app:
```bash
python todo_app_themes.py
```

Or for Mac/Linux:
```bash
python3 todo_app_themes.py
```

## 🎨 Using the App

### Add a Task
1. Type your task in the text box
2. (Optional) Pick a due date
3. Click "💖 Add Task" or press Enter

### Mark Complete
- Click task → Click "✓ Mark Completed"

### Edit Task
- Click task → Click "✏️ Edit" → Type new name

### Delete Task
- Click task → Click "🗑 Delete"

### Change Theme
1. Click "⚙️ Theme" button
2. Select your favorite theme
3. Click "✅ Apply Theme"
4. App restarts with new colors!

## 📁 Project Structure

- `todo_app_themes.py` - Main application file
- `requirements.txt` - Python dependencies
- `README.md` - This file

## 🎨 Theme System

The app includes 6 pre-built themes. Your theme preference is saved automatically in `config.json`.

### Available Themes

| Theme | Colors |
|-------|--------|
| 💖 Girly Pink | Hot pink, light pink background |
| 🌙 Dark Mode | Dark gray, perfect for night |
| 🌊 Ocean Blue | Ocean blue, calm and peaceful |
| 💜 Purple Vibes | Soft purple, sophisticated |
| 🌅 Sunset | Coral, warm and cozy |
| 🍃 Mint Fresh | Teal, clean and fresh |

## 📝 How Tasks are Stored

Tasks are saved in `tasks.json`:

```json
[
    {
        "name": "Buy groceries",
        "completed": false,
        "due_date": "2025-04-15"
    },
    {
        "name": "Finish project",
        "completed": true,
        "due_date": "2025-04-10"
    }
]
```

## 🛠️ Technologies Used

- **Python 3** - Programming language
- **Tkinter** - GUI framework
- **tkcalendar** - Calendar widget
- **JSON** - Data storage

## 📚 Learning Concepts

This project teaches:
- Object-Oriented Programming (OOP)
- GUI development with Tkinter
- File I/O and JSON handling
- DateTime operations
- Event handling
- Color themes and UI design

## 💡 Features Explained

### Auto-Save
Every task is automatically saved to `tasks.json`. No need to manually save!

### Theme System
- Click "⚙️ Theme" to open theme selector
- Choose from 6 pre-designed themes
- Your choice is saved to `config.json`
- App remembers your theme next time!

### Due Dates
- Optional due date picker
- Status indicators:
  - 📅 = Regular due date
  - 🔔 = Due today!
  - ⚠️ = Overdue (shown in red)

## 🎓 For Beginners

If you're new to Python and Tkinter:
1. Read the code comments
2. Try modifying colors
3. Change button text
4. Customize themes
5. Build your own features!

## 🚀 Future Enhancements

Ideas for improvements:
- [ ] Add task categories/tags
- [ ] Add priority levels (High/Medium/Low)
- [ ] Add recurring tasks
- [ ] Add task reminders/notifications
- [ ] Add subtasks
- [ ] Export tasks to PDF
- [ ] Dark mode based on system settings
- [ ] Custom color picker

## 🤝 Contributing

Found a bug or want to add a feature?

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created with ❤️ for organizing tasks beautifully!

## 🙏 Credits

Thanks to:
- **Tkinter** for the GUI framework
- **tkcalendar** for the date picker
- **Python** community for amazing tools

## ❓ FAQ

**Q: Can I modify the themes?**
A: Yes! Edit the THEMES dictionary in the code.

**Q: Where are my tasks saved?**
A: In `tasks.json` in the same folder.

**Q: Can I use this at work?**
A: Absolutely! It's completely free and open source.

**Q: How do I share this with friends?**
A: Send them the GitHub link or the folder with all files!

**Q: Can I run this without Python installed?**
A: Yes, using PyInstaller to create an executable file.

## 📞 Support

For help:
1. Contact anjalipandey708438@gmail.com
2. Check closed GitHub issues
3. Create a new GitHub issue

## 🌟 Star This Repo!

If you like this project, please give it a ⭐ on GitHub!

---

**Happy task managing!** 💖✨

Made with ❤️ using Python and Tkinter
