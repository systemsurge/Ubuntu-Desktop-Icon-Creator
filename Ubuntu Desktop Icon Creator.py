#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox
import os
import configparser

# Global data store from your specified layout
app_data_store = {}

def get_installed_apps():
    apps = []
    app_dir = "/usr/share/applications/"
    
    if not os.path.exists(app_dir):
        return apps

    for filename in os.listdir(app_dir):
        if filename.endswith(".desktop"):
            path = os.path.join(app_dir, filename)
            config = configparser.ConfigParser(interpolation=None)
            try:
                config.read(path)
                if 'Desktop Entry' in config:
                    entry = config['Desktop Entry']
                    name = entry.get('Name', filename)
                    # Use your precise logic: strip quotes and split commands
                    exec_cmd = entry.get('Exec', '').split()[0].replace('"', '')
                    icon_name = entry.get('Icon', None)
                    
                    apps.append({"id": filename, "name": name, "exec": exec_cmd, "icon": icon_name})
                    app_data_store[filename] = {"name": name, "exec": exec_cmd, "icon": icon_name}
            except:
                continue
    return sorted(apps, key=lambda x: x['name'])

def create_desktop_icon(app):
    # FORCE the path to the current user's Desktop with your slash-replacement fix
    user_home = os.path.expanduser("~")
    desktop_path = os.path.join(user_home, "Desktop", f"{app['name'].replace('/', '-')}.desktop")
    
    content = f"[Desktop Entry]\nType=Application\nName={app['name']}\nExec={app['exec']}\nIcon={app['icon']}\nTerminal=false"
    
    try:
        with open(desktop_path, "w") as f:
            f.write(content)
        os.chmod(desktop_path, 0o755)
        messagebox.showinfo("Success", "Shortcut created on your Desktop!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not create file: {e}")

def show_app_list():
    root = tk.Tk()
    root.title("Desktop Icon Creator")
    root.geometry("500x600")

    # Keeping your chosen layout frame perfectly intact
    tree = ttk.Treeview(root, columns=("Name"), show="headings")
    tree.heading("Name", text="Application Name")
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Populating from the new list extractor
    apps = get_installed_apps()
    for app in apps:
        # Maps data tuple to headings display while attaching application data to tags
        tree.insert("", "end", iid=app['id'], values=(app['name'],), tags=(app,))

    def on_button_click():
        selected = tree.selection()
        if selected:
            # Resolves item directly via your app_data_store index mapping
            create_desktop_icon(app_data_store[selected[0]])
        else:
            messagebox.showwarning("Selection Required", "Please highlight an item from the app list first.")

    btn = tk.Button(root, text="Create ICON", command=on_button_click)
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_app_list()
