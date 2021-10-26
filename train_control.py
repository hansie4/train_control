import PySimpleGUI as sg
import subprocess as sp
import serial

runFlag = False # flag for execution

# Open port for serial communication
try:
    ser = serial.Serial(
                            port="COM1",
                            baudrate=9600,
                            bytesize= serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE
                        )
    runFlag = True
except:
    print("Could not connect to port COM1")
    input("Press enter to continue...")

if runFlag:

    print("Port: ", ser.port)

    # Create the GUI
    sg.theme('SystemDefault')
    layout = [  [
                    [sg.Button('Ring Bell')],
                    [sg.Button('Horn')],
                    [sg.Button('Start')],
                    [sg.Button('Brake')],
                    [sg.Button('Accelerate')],
                    [sg.Button('Decelerate')]
                ]
            ]

    window = sg.Window('Train Control', layout)

    def sendCommand(command):
        print("Bytes written: ",ser.write(int(command, 2).to_bytes(len(command) // 8, byteorder='big')), " ", command)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        elif event == 'Ring Bell':
            print('Ringing Bell...')
            sendCommand("111111100000101110011101")
        elif event == 'Start':
            print('Start')
            sendCommand("111111100000101111100011")
        elif event == 'Accelerate':
            print('Accelerate')
            sendCommand("111111100000101110000100") # boost
            sendCommand("111111100000101111001000")
        elif event == 'Decelerate':
            print('Decelerate')
            sendCommand("111111100000101111000010")
        elif event == 'Brake':
            print('Brake')
            sendCommand("111111100000101110000111")
        elif event == 'Horn':
            print('Horn')
            sendCommand("111111100000101110011100")


    ser.close()
    window.close()
