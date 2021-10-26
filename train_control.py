import PySimpleGUI as sg
import subprocess as sp
import serial

runFlag = False # flag for execution

# Commands
ringbell = "111111100000101110011101"
horn = "111111100000101110011100"
start = "111111100000101111100011"
trainBrake = "111111100000101110000111"
boost = "111111100000101110000100"
trainAcc = "111111100000101111001000"
trainDec = "111111100000101111000010"
toggleDir = "111111100000101110000001"
stop = "111111100000101111100000"

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
                    [sg.Button('Ring Bell'), sg.Text('Toggles bell')],
                    [sg.Button('Horn'), sg.Text('Sounds horn')],
                    [sg.Button('Start'), sg.Text('Starts engine at low speed')],
                    [sg.Button('Brake'), sg.Text('Taps the brakes')],
                    [sg.Button('Accelerate'), sg.Text('Accelerates the train')],
                    [sg.Button('Decelerate'), sg.Text('Decelerates the train')],
                    [sg.Button('Toggle Direction'), sg.Text('Toggeles train direction')],
                    [sg.Button('Stop'), sg.Text('Stops the train')]
                ]
            ]

    window = sg.Window('Train Control', layout, resizable=True, size=(300,300))

    def sendCommand(command):
        print("Bytes written: ",ser.write(int(command, 2).to_bytes(len(command) // 8, byteorder='big')), " ", command)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        # Writing commands for each button press
        elif event == 'Ring Bell':
            print('Ringing Bell...')
            sendCommand(ringbell)
        elif event == 'Start':
            print('Start')
            sendCommand(start)
        elif event == 'Accelerate':
            print('Accelerate')
            sendCommand(boost) # boost
            sendCommand(trainAcc)
        elif event == 'Decelerate':
            print('Decelerate')
            sendCommand(trainDec)
        elif event == 'Brake':
            print('Brake')
            sendCommand(trainBrake)
        elif event == 'Horn':
            print('Horn')
            sendCommand(horn)
        elif event == 'Toggle Direction':
            print('Toggle Direction')
            sendCommand(toggleDir)
            sendCommand(start)
        elif event == 'Stop':
            print('Stopping')
            sendCommand(stop)


    ser.close()
    window.close()
