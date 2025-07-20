#  Natural Language to SQL Query App

This project lets you ask questions in **plain English** and automatically converts them into **SQL queries** using **Google's Gemini LLM**. It runs the queries on a **SQLite3 database (`students.db`)** and shows results in a simple web interface using **Streamlit**.

---

##  Overview

No need to learn SQL — just ask:
> "Who scored the highest in each class?"

This app:
- Converts your English question to an SQL query using **Gemini**
- Executes the query on a SQLite database
- Displays the result directly on the screen
- Helps debug errors in SQL if any occur

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/nl-to-sql-app.git
cd nl-to-sql-app
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

---

##  .env Configuration

Create a `.env` file in the root directory with your Gemini API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

---

## students.db — Your Sample Database

The project uses a sample database called `students.db` created using `sqlite3`. To create it:

###  Run:
```bash
python sql.py
```

###  This will:
- Create a table called `students`
- Insert sample student data

###  Table Schema:
```sql
CREATE TABLE students (
    name VARCHAR(30),
    class VARCHAR(20),
    section VARCHAR(25),
    marks INT
);
```

###  Sample Data Inserted:
| name         | class | section | marks |
|--------------|-------|---------|-------|
| John Doe     | 10    | A       | 85    |
| Priya Sharma | 9     | B       | 91    |
| Amit Patel   | 10    | C       | 78    |
| Sneha Mehta  | 8     | A       | 88    |
| Ravi Verma   | 9     | C       | 82    |

---

##  How to Use

1. Run the app:
   ```bash
   streamlit run app.py
   ```

2. Enter a natural language query like:
   - “Who scored highest in class 9?”
   - “List students with marks more than 80.”
   - “Show all students from section A.”

3. The app will:
   - Send your input + schema to Gemini
   - Convert to SQL and clean the query
   - Run it on `students.db`
   - Display the result
   - If there's an error, it helps debug the SQL

---

##  Technologies Used

- **Python**
- **Streamlit** – for the web UI
- **Google Gemini API** – to convert English to SQL
- **SQLite3** – for local database and query execution
- **dotenv** – to manage environment variables

---

##  Example Queries

> “See who is first in every class”  
> “Show names of students who scored more than 90”  
> “Find students in section A from class 10”  


