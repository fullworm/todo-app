import PySimpleGUI
import os

tasks = []

layout = [[sg.Button(button_text= "Add", key='-add-'), sg.Button(button_text= "Remove", key='-remove-')],
          [sg.Listbox(tasks, size=(70,30), no_scrollbar=True, key='-list-')]]

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
            tasks.append(Addtask)
            window['-list-'].update(tasks)

window.close()
