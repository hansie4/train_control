@echo off
SET filename=./dist/GUI/GUI.exe
if exist %filename% (
    start %filename%
) else (
    echo %filename% missing!
    pause
)
exit