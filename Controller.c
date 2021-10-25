#include <stdio.h>
#include <windows.h>
#include <conio.h>

int main(int argc, char *argv[])
{
    // Define the 3 bytes to send
    char bytes_to_send[3];
    bytes_to_send[0] = 0xFE;
    bytes_to_send[1] = 0x00;
    bytes_to_send[2] = 0x00;

    //TODO
    // CHANGE BYTES TO SEND BASED ON argv[1]

    // printf(argv[1]);
    // printf("\n");
    // printf("Press key to continue: ");
    // getch();

    if (strcmp(argv[1], "ring"))
    {
        // Ring the bell
        // 00AAAAAAACCDDDDD
        // 000010111 0011101 assuming train id #23
        bytes_to_send[1] = 0x0b;
        bytes_to_send[2] = 0x9d;
    }
    else if (strcmp(argv[1], "start"))
    {
        // Start the train
        // 00AAAAAAACCDDDDD
        // 000010111 0000100 assuming train id #23,engine boost i suppose.
        bytes_to_send[1] = 0x0b;
        bytes_to_send[2] = 0x84;
    }
    else if (strcmp(argv[1], "acc"))
    {
        // Accelerate the train
        // 00AAAAAAACCDDDDD
        // 0000101111000110 assuming train id #23, accelerate the train by 1(5= no change, 5+1=6)
        bytes_to_send[1] = 0x0b;
        bytes_to_send[2] = 0xc6;
    }
    else if (strcmp(argv[1], "move"))
    {
        // Move the train
        //00AAAAAAACCDDDDD
        //Not sure yet.
        
    }
    else if (strcmp(argv[1], "dec"))
    {
        // Decelerate the train
        // 00AAAAAAACCDDDDD
        // 0000101111000100 assuming train id #23,deceleration by 1(5-1=4)
        bytes_to_send[1] = 0x0b;
        bytes_to_send[2] = 0xc4;
    }
    else if (strcmp(argv[1], "stop"))
    {
        // Stop the train
        // 00AAAAAAACCDDDDD
        // 000010111 1100000 assuming train id #23,setting absolute speed to 0 is also reasonable.
        //bytes_to_send[1] = 0x0b;
        //bytes_to_send[2] = 0xe0;
        //00AAAAAAACCDDDDD
        //000010111 0000111 engine brake also works?
        bytes_to_sent[1] = 0x0b;
        bytes_to_sent[2] = 0x87;
    }

    // Declare variables and structures
    HANDLE hSerial;
    DCB dcbSerialParams = {0};
    COMMTIMEOUTS timeouts = {0};

    // Open the highest available serial port number
    fprintf(stderr, "Opening serial port...");
    hSerial = CreateFile(
        "\\\\.\\COM1", GENERIC_READ | GENERIC_WRITE, 0, NULL,
        OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hSerial == INVALID_HANDLE_VALUE)
    {
        fprintf(stderr, "Error\n");
        return 1;
    }
    else
        fprintf(stderr, "OK\n");

    // Set device parameters (38400 baud, 1 start bit,
    // 1 stop bit, no parity)
    dcbSerialParams.DCBlength = sizeof(dcbSerialParams);
    if (GetCommState(hSerial, &dcbSerialParams) == 0)
    {
        fprintf(stderr, "Error getting device state\n");
        CloseHandle(hSerial);
        return 2;
    }

    dcbSerialParams.BaudRate = CBR_9600;
    dcbSerialParams.ByteSize = 8;
    dcbSerialParams.StopBits = ONESTOPBIT;
    dcbSerialParams.Parity = NOPARITY;
    if (SetCommState(hSerial, &dcbSerialParams) == 0)
    {
        fprintf(stderr, "Error setting device parameters\n");
        CloseHandle(hSerial);
        return 3;
    }

    // Set COM port timeout settings
    timeouts.ReadIntervalTimeout = 50;
    timeouts.ReadTotalTimeoutConstant = 50;
    timeouts.ReadTotalTimeoutMultiplier = 10;
    timeouts.WriteTotalTimeoutConstant = 50;
    timeouts.WriteTotalTimeoutMultiplier = 10;
    if (SetCommTimeouts(hSerial, &timeouts) == 0)
    {
        fprintf(stderr, "Error setting timeouts\n");
        CloseHandle(hSerial);
        return 4;
    }

    // Send specified text (remaining command line arguments)
    DWORD bytes_written, total_bytes_written = 0;
    fprintf(stderr, "Sending bytes...");
    if (!WriteFile(hSerial, bytes_to_send, 3, &bytes_written, NULL))
    {
        fprintf(stderr, "Error\n");
        CloseHandle(hSerial);
        return 5;
    }
    fprintf(stderr, "%d bytes written\n", bytes_written);

    // Close serial port
    fprintf(stderr, "Closing serial port...");
    if (CloseHandle(hSerial) == 0)
    {
        fprintf(stderr, "Error\n");
        return 6;
    }
    fprintf(stderr, "OK\n");

    // exit normally
    return 0;
}
