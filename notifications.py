import os
from time import sleep
from win10toast import ToastNotifier

# Define dictionaries
directories = {
    "Folder0":"C:\\Users\\Adrian\\Desktop\\test",
    "Folder1":"C:\\Users\\Adrian\\Desktop\\test1"
    # .
    # .
    # .
    # Add more folders if desired
}

# Define toaster
toaster = ToastNotifier()

while True:
    for directory,path in directories.items():
        if os.path.exists(path):
            files = os.listdir(path)

            for file in files:
                toaster.show_toast(directory + " (" + path + ")", file,
                    icon_path="python.ico",
                    duration=10,
                    threaded=True
                )

                while toaster.notification_active():sleep(0.1)

        else:
            toaster.show_toast("Error: " + directory + " (" + path + ")", "Sorry but this directory doesn't exist!",
                icon_path="python.ico",
                duration=30,
                threaded=True
            )

        while toaster.notification_active():sleep(0.1)

        # Sleep for 30minutes
        sleep(1800)
