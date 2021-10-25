import PySimpleGUI as sg
import subprocess as sp
import serial

sg.theme('SystemDefault')   # Add a touch of color
# All the stuff inside your window.
layout = [  [
                [sg.Button('Ring Bell')],
                [sg.Button('Start')],
                [sg.Button('Accelerate')],
                [sg.Button('Move')],
                [sg.Button('Decelerate')],
                [sg.Button('Stop Train')]
            ]
        ]

# Create the Window
window = sg.Window('Train Control', layout)

ser = serial.Serial(
                        port="COM1",
                        baudrate=9600,
                        bytesize= serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE
                    )

print("Port: ", ser.port)

output = "111111100000101110011101"

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    elif event == 'Ring Bell':
        print('Ringing Bell...')
        output = "111111100000101110011101"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Start':
        print('Start')
        output = "111111100000101110011101"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Accelerate':
        print('Accelerate')
        output = "111111100000101110011101"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Move':
        print('Move')
        output = "111111100000101110011101"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Decelerate':
        print('Decelerate')
        output = "111111100000101110011101"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Stop Train':
        print('Stop Train')
        output = "111111100000101110011101"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)


ser.close()
window.close()
