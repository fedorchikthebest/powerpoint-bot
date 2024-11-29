@echo off
set "pythonpath=python.exe" # сюда путь для питона в венве

:loop
%pythonpath% bot.py
del ".\presentations\*.pdf"
goto :loop

pause