@echo off
SET filename=./dist/train_control/train_control.exe
if exist %filename% (
    start %filename%
) else (
    echo %filename% missing!
    pause
)
exit