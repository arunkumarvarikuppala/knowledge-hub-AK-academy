from getpass import getpass

from database import initialize_database, create_teacher

initialize_database()

print("\nKnowledge Hub - Teacher Account Setup")
print("------------------------------------")

username = input("Teacher username [arunkumar]: ").strip()
username = username or "arunkumar"

password = getpass("Create your teacher password: ")
confirm = getpass("Confirm your teacher password: ")

if password != confirm:
    print("Passwords do not match. Please try again.")
elif len(password) < 12:
    print("Use at least 12 characters for your password.")
else:
    success, message = create_teacher(username, password)
    print(message)