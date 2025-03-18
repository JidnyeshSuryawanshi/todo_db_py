import mysql.connector as mysql
print("hello World")

con=mysql.connect(host="localhost",user="root",passwd="Hello@26")

print("Connection established?")

cursor=con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS TEST01")

print("Databse created!")

cursor.execute("USE TEST01")
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")
 
print("Table created...")

cursor.execute("SHOW TABLES")
 
for i in cursor:
    print(i)
 
# print("Table created...")
 
while True:
    print("\n Task Management")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        task = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        print("✅ Task added successfully!")
        con.commit() 
    
    elif choice == "2":
        cursor.execute("SELECT * FROM tb_todo")
        tasks = cursor.fetchall()
        if tasks:
            print("Tasks here aree:")
            for task in tasks:
                print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")
        else:
            print("Task nOT found.")
    
    elif choice == "3":
        task_id = input("Enter task ID to update: ")
        new_status = input("Enter new status (pending/ or completed): ")
        cursor.execute("UPDATE tb_todo SET status = %s WHERE id = %s", (new_status, task_id))
        con.commit()
        print(f"✅ Task ID {task_id} updated to {new_status}")
    
    elif choice == "4":
        task_id = input("Enter task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id = %s", (task_id,))
        con.commit()
        print(f"✅ Task ID {task_id} deleted")
 
    elif choice == "5":
        print("Exiting Task Management...")
        break
 
    else:
        print("Invalid choice. Please try again.")
 
con.close()