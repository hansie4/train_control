import PySimpleGUI as sg
import subprocess as sp
import serial

sg.theme('SystemDefault')   # Add a touch of color
# All the stuff inside your window.
layout = [  [
                [sg.Button('Ring Bell')],
                [sg.Button('Start')],
                [sg.Button('Accelerate')],
                [sg.Button('Decelerate')],
                [sg.Button('Stop Train')],
                [sg.Button('Brake')],
                [sg.Button('Horn')]
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
        output = "111111100000101111100001"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Accelerate':
        print('Accelerate')
        output = "111111100000101111000110"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Decelerate':
        print('Decelerate')
        output = "111111100000101111000100"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Stop Train':
        print('Stop Train')
        output = "111111100000101111100000"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Brake':
        print('Brake')
        output = "111111100000101110000111"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)
    elif event == 'Horn':
        print('Horn')
        output = "111111100000101110011100"
        print("Bytes written: ",ser.write(int(output, 2).to_bytes(len(output) // 8, byteorder='big')), " ", output)


ser.close()
window.close()
