import PySimpleGUI as sg
import subprocess as sp

sg.theme('SystemDefault')   # Add a touch of color
# All the stuff inside your window.
layout = [  [
                [sg.Button('Ring Bell')],
                [sg.Button('Start')],
                [sg.Button('Accelerate')]
            ],
            [
                [sg.Button('Move')],
                [sg.Button('Decelerate')],
                [sg.Button('Stop Train')]
            ],
            [sg.Text(text = "Status", background_color = "gray", key="status")]]

# Create the Window
window = sg.Window('Train Control', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    elif event == 'Ring Bell':
        print('Ringing Bell...')
        returnVal = sp.run(["./Controller.exe", "ring"])
        if(returnVal == 0):
            window["status"].update("Success")
        else:
            window["status"].update("Failed")
        print(returnVal)
    elif event == 'Start':
        print('Start')
        returnVal = sp.call(["./Controller.exe", "start"])
        if(returnVal == 0):
            window["status"].update("Success")
        else:
            window["status"].update("Failed")
        print(returnVal)
    elif event == 'Accelerate':
        print('Accelerate')
        returnVal = sp.call(["./Controller.exe", "acc"])
        if(returnVal == 0):
            window["status"].update("Success")
        else:
            window["status"].update("Failed")
        print(returnVal)
    elif event == 'Move':
        print('Move')
        returnVal = sp.call(["./Controller.exe", "move"])
        if(returnVal == 0):
            window["status"].update("Success")
        else:
            window["status"].update("Failed")
        print(returnVal)
    elif event == 'Decelerate':
        print('Decelerate')
        returnVal = sp.call(["./Controller.exe", "dec"])
        if(returnVal == 0):
            window["status"].update("Success")
        else:
            window["status"].update("Failed")
        print(returnVal)
    elif event == 'Stop Train':
        print('Stop Train')
        returnVal = sp.call(["./Controller.exe", "stop"])
        if(returnVal == 0):
            window["status"].update("Success")
        else:
            window["status"].update("Failed")
        print(returnVal)

window.close()
