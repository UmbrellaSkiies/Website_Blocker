import tkinter as tk
import time
from datetime import datetime as dt
import platform

def block_websites():
    start_time = dt(dt.now().year, dt.now().month, dt.now().day, int(start_hour.get()), int(start_minute.get()))
    end_time = dt(dt.now().year, dt.now().month, dt.now().day, int(end_hour.get()), int(end_minute.get()))
    blocked_websites = websites_entry.get("1.0", tk.END).strip().split("\n")

    while True:
        if start_time < dt.now() < end_time:
            try:
                with open(hosts_path, "r+") as file:
                    content = file.read()
                    for website in blocked_websites:
                        if website not in content:
                            file.write("127.0.0.1 " + website + "\n")
                status_label.config(text="Websites blocked.")
            except PermissionError:
                status_label.config(text="Permission denied. Run the script as an administrator/superuser.")
            except Exception as e:
                status_label.config(text="An error occurred: " + str(e))
        else:
            try:
                with open(hosts_path, "r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in blocked_websites):
                            file.write(line)
                    file.truncate()
                status_label.config(text="Websites unblocked.")
            except PermissionError:
                status_label.config(text="Permission denied. Run the script as an administrator/superuser.")
            except Exception as e:
                status_label.config(text="An error occurred: " + str(e))

        time.sleep(5)


# Define the path of the hosts file based on the operating system
hosts_path = ""
system = platform.system()
if system == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif system == "Linux" or system == "Darwin":
    hosts_path = "/etc/hosts"
else:
    print("Unsupported operating system.")
    exit()

# Create the UI window
window = tk.Tk()
window.title("Website Blocker")

# Start time labels and inputs
start_hour_label = tk.Label(window, text="Start Hour:")
start_hour_label.pack()
start_hour = tk.Entry(window)
start_hour.pack()

start_minute_label = tk.Label(window, text="Start Minute:")
start_minute_label.pack()
start_minute = tk.Entry(window)
start_minute.pack()

# End time labels and inputs
end_hour_label = tk.Label(window, text="End Hour:")
end_hour_label.pack()
end_hour = tk.Entry(window)
end_hour.pack()

end_minute_label = tk.Label(window, text="End Minute:")
end_minute_label.pack()
end_minute = tk.Entry(window)
end_minute.pack()

# Websites entry
websites_label = tk.Label(window, text="Websites to block (one per line):")
websites_label.pack()
websites_entry = tk.Text(window, height=5, width=30)
websites_entry.pack()

# Status label
status_label = tk.Label(window, text="")
status_label.pack()

# Block button
block_button = tk.Button(window, text="Start Blocking", command=block_websites)
block_button.pack()

window.mainloop()