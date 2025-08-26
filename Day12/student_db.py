import sqlite3
from rich.console import Console
from rich.table import Table

console = Console()


def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()


def insert_student(name, age, grade):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()
    console.print(f"[green]Student {name} added successfully![/green]")

def fetch_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    table = Table(title="Student Database")
    table.add_column("ID", justify="right")
    table.add_column("Name", style="cyan")
    table.add_column("Age", style="yellow")
    table.add_column("Grade", style="magenta")

    for row in rows:
        table.add_row(str(row[0]), row[1], str(row[2]), row[3])

    console.print(table)

def update_student(student_id, name=None, age=None, grade=None):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE students SET name = ? WHERE id = ?", (name, student_id))
    if age:
        cursor.execute("UPDATE students SET age = ? WHERE id = ?", (age, student_id))
    if grade:
        cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (grade, student_id))
    conn.commit()
    conn.close()
    console.print(f"[blue]Student ID {student_id} updated![/blue]")

def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    console.print(f"[red]Student ID {student_id} deleted![/red]")


def menu():
    create_table()
    while True:
        console.print("\n[bold yellow]--- Student Database Menu ---[/bold yellow]")
        console.print("1. Add Student")
        console.print("2. View Students")
        console.print("3. Update Student")
        console.print("4. Delete Student")
        console.print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            insert_student(name, age, grade)

        elif choice == "2":
            fetch_students()

        elif choice == "3":
            sid = int(input("Enter student ID to update: "))
            new_name = input("Enter new name (or press Enter to skip): ")
            new_age = input("Enter new age (or press Enter to skip): ")
            new_grade = input("Enter new grade (or press Enter to skip): ")

            update_student(
                sid,
                name=new_name if new_name else None,
                age=int(new_age) if new_age else None,
                grade=new_grade if new_grade else None
            )

        elif choice == "4":
            sid = int(input("Enter student ID to delete: "))
            delete_student(sid)

        elif choice == "5":
            console.print("[bold green]Goodbye![/bold green]")
            break

        else:
            console.print("[red]Invalid choice! Try again.[/red]")

if __name__ == "__main__":
    menu()
