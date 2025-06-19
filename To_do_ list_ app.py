import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import tkinter.font as tkfont

#Font
title_font= ("Helvetica", 18, "bold")
task_font= ("Segoe UI", 12)
button_font=("Segoe UI", 10, "bold")

#window
window= tk.Tk()
window.title("To-Do List App")
window.geometry("850x450")

#top frame
top_frame=tk.Frame(window)
top_frame.pack(pady=10)

#title label 
title_label= ttk.Label(top_frame, text= "TASKS", font=title_font)
title_label.pack()

#inputfield
entry_string=tk.StringVar()
entry= ttk.Entry(window,font=task_font, textvariable=entry_string, width=40,)
entry.pack(pady=(0,10))
entry_string.set("")

#list box to display tasks
list_frame= tk.Frame(window)
list_frame.pack(pady=10)
scrollbar=tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox=tk.Listbox(master=list_frame, font=task_font, width= 50, height=8, yscrollcommand=scrollbar.set)
task_listbox.pack(side=tk.LEFT, pady=10)
scrollbar.config (command=task_listbox.yview)

#task storage
tasks=[]

#FUNCTIONS
#add function
def add_task():
    new_task= entry_string.get().strip()
    entry.delete(0, tk.END)
    if new_task:
        tasks.append(new_task)
        task_listbox.insert(tk.END, new_task)
        entry_string.set("")

#delete function
def delete_task():
    selected=task_listbox.curselection()
    if selected:
        index=selected[0]
        task_listbox.delete(index)
        tasks.pop(index)
        entry_string.set("")

#mark task done function
def mark_task_done():
    selected=task_listbox.curselection()
    if selected:
        index=selected[0]
        current_text=task_listbox.get(index)
        if not current_text.endswith("✅"):
            done_text=current_text+"✅"
            task_listbox.delete(index)
            task_listbox.insert(index, done_text)
            tasks[index]=done_text
        
#update function
def update_task():
    selected= task_listbox.curselection()
    if selected:
        index=selected[0]
        new_text=entry_string.get().strip()
        if new_text:
            task_listbox.delete(index)
            task_listbox.insert(index, new_text)
            tasks[index]= new_text
            entry_string.set ("")

#load function
def load_selected_task(event):
    selected=task_listbox.curselection()
    if selected:
        index=selected[0]
        entry_string.set(task_listbox.get(index))
task_listbox.bind("<<ListboxSelect>>", load_selected_task)

#clear all function
def clear_all_tasks():
    confirm=messagebox.askyesno("Clear All, Are you sure you want to delete all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)
        tasks.clear()
        entry_string.set("")

#BUTTONS
button_frame=tk.Frame(window)
button_frame.pack(pady=18)

#add button        
add_button=tk.Button(button_frame, text="Add Task", font=button_font, command= add_task, bg="#444", fg="white", activebackground="#666", borderwidth=0)
add_button.pack(side=tk.LEFT, padx=12)

#delete button
delete_button= tk.Button(button_frame, text="Delete", command=delete_task, bg="#444", fg="white", activebackground="#666", borderwidth=0)
delete_button.pack(side=tk.LEFT, padx=12)

#mark as done button
done_button=tk.Button(button_frame, text= "Mark As Done", command= mark_task_done, bg="#444", fg="white", activebackground="#666", borderwidth=0)
done_button.pack(side=tk.LEFT, padx=12)

#update button
update_button=tk.Button(button_frame, text="Update", command= update_task, bg="#444", fg="white", activebackground="#666", borderwidth=0)
update_button.pack(side=tk.LEFT, padx=12)

#clear all button
clear_all_button=tk.Button(button_frame, text="Clear All", command= clear_all_tasks, bg="#444", fg="white", activebackground="#666", borderwidth=0)
clear_all_button.pack(side=tk.LEFT, padx=12)
    
window.mainloop()






        








