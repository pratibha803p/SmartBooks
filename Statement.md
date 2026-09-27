# SmartBook - Project Statement

## Problem Statement

In today's digital age, readers often struggle to keep track of their book collections and maintain a personalized list of books they want to read or have read. Many people find it challenging to:

- **Organize** their reading preferences efficiently
- **Search** through available books by title or author
- **Remember** which books are their favorites
- **Access** book recommendations in a structured manner

## Objective

SmartBook aims to provide a simple yet effective command-line solution for readers to:

1. Create personalized user accounts
2. Browse through a curated book catalog
3. Search for books quickly and efficiently
4. Maintain a personalized list of favorite books
5. Access detailed information about each book

## Target Users

- **Students** looking for inspirational and educational books
- **Book enthusiasts** who want to organize their reading preferences
- **UPSC/Civil Services aspirants** seeking curated book recommendations
- **Casual readers** who want a simple book management system

## Key Features

### 1. User Authentication System
- Users can create unique profiles with username and password
- Secure login mechanism to protect personal data
- Each user has an isolated favorites list

### 2. Book Catalog Management
- Pre-loaded catalog of 5 carefully selected books
- Books categorized by genre (Fiction, Autobiography, Inspiration, History)
- Each book includes metadata:
  - Title
  - Author
  - Category
  - Usefulness information

### 3. Search Functionality
- Search for books using either Title or Author
- The ignores capital letters, so "python" matches "Python"
- Displays the matching books immediately along with their details

### 4. Favorites Management
- Add books to your personal favorites list with a single action
- Access and review your saved list whenever needed
- Automatically checks to make sure the same book isn't saved twice
- Keeps your saved favorites intact even after closing the program

## Technical Architecture

### Technology Stack
- **Language**: Python 3
- **Data Storage**: JSON (file-based)
- **Interface**: Command-line (CLI)

