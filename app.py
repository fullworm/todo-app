import PySimpleGUI as sg
import os
import funcs as fc

path = "tasks.txt"

tasks = fc.ReadFile(path)

listbox = sg.Listbox(tasks, size=(70,30), no_scrollbar=True, key='-list-', enable_events=True, font=('Calibri',14))
layout = [[sg.Button(button_text= "Add", key='-add-'), sg.Button(button_text= "Remove", key='-remove-')],
          [listbox]]

window = sg.Window("Todo App", layout)



RUN = True
while RUN:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        RUN = False
    if event == '-add-':
        Addtask = sg.popup_get_text(message="Name a task")
        if Addtask == '':
            sg.popup("Please enter a valid task")
        else:
            tasks.append(f"({len(tasks)+1}) " + Addtask)
            fc.WriteList(tasks, path)
            window['-list-'].update(tasks)
    if event =='-remove-':
        selected = listbox.get()[0]
        tasks.remove(selected)
        window['-list-'].update(tasks)



window.close()
