import PySimpleGUI as sg
import funcs as fc

path = "tasks.txt"

tasks = fc.ReadFile(path)

List_box = sg.Listbox(tasks, size=(70,30), no_scrollbar=True, key='-list-', enable_events=True, font=('Calibri',14))

layout = [[sg.Button(image_source="plus.png", key='-add-'), sg.Button(image_source="minus.png", key='-remove-'), sg.Button(button_text="Clear", key="-clear-")],
          [List_box]]

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
        if values['-list-']:
            selected = values['-list-'][0]
            tasks.remove(selected)
            window['-list-'].update(tasks)
        else:
            sg.popup("Please select a task for removal")
    if event == '-clear-':
        tasks.clear()
        fc.ClearList(path)
        window['-list-'].update(tasks)

window.close()
