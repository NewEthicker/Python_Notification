# Before running the code install these libraries : #
             # pip install plyer #
         # pip install notification #

from plyer import notification
def show_notification():
    title = input("Enter notification title: ")
    message = input("Enter notification message: ")
    duration = int(input("Enter duration in seconds: "))
    notification.notify(title=title, message=message, timeout=duration)
while True:
    print("1. Show Notification")
    print("2. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_notification()
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")
