
# Friend Finder

Friend Finder is a Python-based application that helps students find compatible buddies based on their preferences and interests. This project uses Tkinter for the graphical user interface and SQLite for managing data. It features a scoring system that compares user preferences and calculates compatibility using statistical methods.

---

## Features

- **User Authentication:** Secure login functionality using an SQLite database.
- **Student Management:** Add, delete, and manage student information.
- **Preference Matching:** Compare preferences between two students and determine compatibility.
- **Dynamic Questions:** Easily configurable questions about preferences and activities.
- **Activity Ranking:** Allows students to rate activities, with results saved to a database.
- **Compatibility Score:** Calculates and displays the compatibility percentage between two students.
- **Database Integration:** Supports multiple SQLite databases (`LoginDB.db` and `Student.db`).

---

## Requirements

### Libraries

The project requires the following Python libraries:

- `tkinter`: For the graphical user interface.
- `sqlite3`: For managing the database.

### Files

The following files must be present in the project directory:

1. **Python Script**: `friend_finder.py` - The main application script.
2. **Image File**: `friend.png` - Displayed on the login screen.
3. **Database Files**:
   - `LoginDB.db` - Stores user login credentials.
   - `Student.db` - Stores student data and answers.
4. **Questions File**: `Questions.txt` - Contains activities/questions students can rate.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd friend-finder
   ```

2. **Install Python:**
   Ensure you have Python 3.8 or higher installed on your system.

3. **Install Required Libraries:**
   The required libraries are included in Python's standard library, so no additional installation is needed.

4. **Add Required Files:**
   Ensure the following files are in the project folder:
   - `friend_finder.py`
   - `friend.png`
   - `LoginDB.db`
   - `Student.db`
   - `Questions.txt`

5. **Run the Application:**
   ```bash
   python friend_finder.py
   ```

---

## Usage

1. **Login:**
   - Enter your username and password.
   - Click "Submit" to log in.

2. **Manage Students:**
   - Add new student details, including Student ID, First Name, Surname, Nationality, and Grade.
   - Delete student records if needed.

3. **Answer Questions:**
   - Navigate to the "Questions" tab and select a student.
   - Rate activities on a scale of 1 to 10.
   - Save answers to the database.

4. **Compare Compatibility:**
   - Choose two students to compare.
   - View the compatibility score based on their activity ratings.

---

## Questions

The file `Questions.txt` contains the following predefined questions that students rate on a scale from 1 to 10:

1. Like STEM fields  
2. Like Humanities  
3. Like to talk  
4. Playing computer games  
5. Like dogs or cats  
6. Watching comedy  
7. Going to cafe  
8. I go to church regularly.  
9. Like dancing  
10. Like cooking  
11. Enjoy eating food  
12. Want to study in the United States

You can modify this file to include additional questions or customize existing ones.

---

## Code Structure

1. **`friend_finder.py`:**
   - Handles the user interface and logic.
   - Includes subroutines for managing students, calculating compatibility, and database interactions.

2. **Databases:**
   - `LoginDB.db`: Stores user credentials.
   - `Student.db`: Stores student profiles, grades, and activity ratings.

3. **Images:**
   - `friend.png`: Displayed on the login screen.

4. **Questions:**
   - `Questions.txt`: A configurable list of activities/questions.

---

## Compatibility Scoring

The application uses statistical methods (e.g., ranking and correlation) to calculate compatibility:

- **Perfect Choice:** ≥ 90%
- **Reasonable Choice:** ≥ 50%
- **Not the Best Choice:** ≥ 30%
- **Poor Choice:** ≥ -50%
- **Worst Choice:** < -50%

---

## Future Enhancements

- Add user registration functionality.
- Enable data export/import for analysis.
- Improve the user interface with additional themes.
- Enhance security by hashing passwords.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.
