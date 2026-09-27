# SmartBook - Personal Book Management System

A simple yet powerful command-line application to manage your personal book collection, search for books, and maintain a personalized list of favorites.

## Features

**User Authentication**
- Create your own profile with username and password
- Secure login to access your personal book collection

**Book Catalog**
- Browse a curated collection of inspiring and educational books
- Each book includes title, author, category, and details about its usefulness

**Search Functionality**
- Search books by title or author name
- Quick access to book information and categories

**Favorites Management**
- Add books to your personal favorites list
- View all your favorite books anytime
- Remove books from favorites if needed

## Installation

### Requirements
- Python 3.6 or higher
- No external dependencies required (uses only built-in libraries)

### Setup

1. **Clone or download the project**
```bash
git clone <repository-url>
cd smartbook
```

2. **Run the application**
```bash
python smartbook_fixed.py
```

## How to Use

### First Time Users
1. Launch the application
2. Select **"Create New Profile"** from the main menu
3. Enter a username and password
4. Access the user menu

### Existing Users
1. Launch the application
2. Select **"Login"**
3. Enter your username and password
4. Access the user menu

### User Menu Options

| Option | Description |
|--------|-------------|
| 1 | View all books in the catalog |
| 2 | Search for a book by title or author |
| 3 | Add a book to your favorites |
| 4 | View your favorite books |
| 5 | Logout

## Available Books

1. **Harry Potter And The Sorcerer's Stone** - J.K. Rowling (Fiction/Fantasy)
   - Useful for: Imagination and English skills

2. **The Alchemist** - Paulo Coelho (Inspiration)
   - Useful for: Motivation and Life Goals

3. **Wings Of Fire** - A.P.J. Abdul Kalam (Autobiography)
   - Useful for: Inspiration and Career Growth

4. **The Diary Of Young Girl** - Anne Frank (History/Biography)
   - Useful for: Understanding History and Emotion

5. **Head Held High** - Vishwas Nangre Patil (Autobiography/Inspirational)
   - Useful for: UPSC and Civil Services Aspirants

## File Structure

smartbook/
├── smartbook_fixed.py # Main application file    
├── smartbook_data.json # User profiles & favorites (auto-generated)  
├── README.md # This file  
├── statement.md # Project statement  
└── .gitignore # Git ignore file  


## Data Storage

- User profiles and favorite lists are stored in `smartbook_data.json`
- This file is created automatically on first use
- Do NOT commit this file to version control (it contains user data)

## Project Information

- **Language**: Python
- **Type**: Console Application
- **Version**: 1.0
- **Status**: Active Development
---
Your output should look like this:

<img width="1280" height="687" alt="Screenshot (127)" src="https://github.com/user-attachments/assets/2207baf6-37b5-40c8-9ae7-37cd1a240347" />
