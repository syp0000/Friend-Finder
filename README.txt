Friend Finder
- Friend Finder is a Python-based application that helps students find compatible buddies based on their preferences and interests. This project uses Tkinter for the graphical user interface and SQLite for managing data. It features a scoring system that compares user preferences and calculates compatibility using statistical methods.

Features
- User Authentication: Secure login functionality using an SQLite database.
- Student Management: Add, delete, and manage student information.
- Preference Matching: Compare preferences between two students and determine compatibility.
-- Dynamic Questions: Easily configurable questions about preferences and activities.
- Activity Ranking: Allows students to rate activities, with results saved to a database.
- Compatibility Score: Calculates and displays the compatibility percentage between two students.
- Database Integration: Supports multiple SQLite databases (LoginDB.db and Student.db).

Requirements

- Libraries
  The project requires the following Python libraries:
  - tkinter: For the graphical user interface.
  - sqlite3: For managing the database.
- Files
  The following files must be present in the project directory:
  - Python Script: friend_finder.py - The main application script.
  - Image File: friend.png - Displayed on the login screen.
  - Database Files:
    - LoginDB.db - Stores user login credentials.
    - Student.db - Stores student data and answers.
  - Questions File: Questions.txt - Contains activities/questions students can rate.

Setup Instructions
- Install Python: Ensure you have Python 3.8 or higher installed on your system.
- Ensure the following files are in the project folder:
    friend_finder.py
    friend.png
    LoginDB.db
    Student.db
    Questions.txt

Usage
- Login:
  - Enter your username and password.
  - Click "Submit" to log in.
- Manage Students:
  - Add new student details, including Student ID, First Name, Surname, Nationality, and Grade.
  - Delete student records if needed.
- Answer Questions:
  - Navigate to the "Questions" tab and select a student.
  - Rate activities on a scale of 1 to 10.
  - Save answers to the database.
- Compare Compatibility:
  - Choose two students to compare.
  - View the compatibility score based on their activity ratings.

Questions
- The file Questions.txt contains the following predefined questions that students rate on a scale from 1 to 10:
  
  Like STEM fields
  Like Humanities
  Like to talk
  Playing computer games
  Like dogs or cats
  Watching comedy
  Going to cafe
  I go to church regularly.
  Like dancing
  Like cooking
  Enjoy eating food
  Want to study in the United States

- You can modify this file to include additional questions or customize existing ones.

Code Structure
- friend_finder.py: Handles the user interface and logic, includes subroutines for managing students, calculating compatibility, and database interactions.
- Databases:
  - LoginDB.db: Stores user credentials.
  - Student.db: Stores student profiles, grades, and activity ratings.
- Image(friend.png): Displayed on the login screen.
- Questions: A configurable list of activities/questions.

Compatibility Scoring
- The application uses statistical methods (e.g., ranking and correlation) to calculate compatibility:
  Perfect Choice: ≥ 90%
  Reasonable Choice: ≥ 50%
  Not the Best Choice: ≥ 30%
  Poor Choice: ≥ -50%
  Worst Choice: < -50%

Future Enhancements
- Add user registration functionality.
- Enable data export/import for analysis.
- Improve the user interface with additional themes.
- Enhance security by hashing passwords.

Credits
- Created by Siyeon Park

License
- This project is licensed under the MIT License.
