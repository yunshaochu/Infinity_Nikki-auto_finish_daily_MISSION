@echo off
%1(start /min cmd.exe /c %0 :& exit )


cd /d D:\A1\nikki-daily_MISSION
D:\myCache\Anaconda3\envs\nikki-daily_MISSION\python.exe app.py