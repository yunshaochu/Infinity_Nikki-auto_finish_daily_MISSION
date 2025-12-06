@echo off
%1(start /min cmd.exe /c %0 :& exit )


cd /d D:\A1\nikki-daily_MISSION
mkdir logs 2>nul
set datetime=%date:~0,4%%date:~5,2%%date:~8,2%
D:\myCache\Anaconda3\envs\nikki-daily_MISSION\python.exe app.py > logs\%datetime%.log 2>&1