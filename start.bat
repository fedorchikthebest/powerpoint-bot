@echo off
set "pythonpath=.\.venv\bin\python.exe" # сюда путь для питона в венве

:loop
%pythonpath% bot.py
goto :loop

pause